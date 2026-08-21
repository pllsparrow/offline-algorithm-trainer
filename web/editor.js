import {defaultKeymap, history, historyKeymap, indentWithTab} from "@codemirror/commands";
import {closeBrackets, closeBracketsKeymap} from "@codemirror/autocomplete";
import {bracketMatching, HighlightStyle, indentUnit, syntaxHighlighting} from "@codemirror/language";
import {python} from "@codemirror/lang-python";
import {EditorState, RangeSetBuilder, StateEffect, StateField} from "@codemirror/state";
import {tags} from "@lezer/highlight";
import nspell from "nspell";
import {
  Decoration,
  EditorView,
  GutterMarker,
  ViewPlugin,
  drawSelection,
  dropCursor,
  gutter,
  highlightActiveLine,
  highlightActiveLineGutter,
  highlightSpecialChars,
  keymap,
  lineNumbers,
} from "@codemirror/view";


const toggleBreakpoint = StateEffect.define();
const replaceBreakpoints = StateEffect.define();
const spellingReady = StateEffect.define();


const SPELLING_EXCLUSIONS = new Set([
  "acm", "args", "argv", "async", "await", "bool", "classmethod", "deque", "dict", "elif", "enum",
  "enumerate", "frozenset", "heapq", "idx", "init", "int", "iter", "json", "kwargs", "kth", "leetcode",
  "list", "memo", "neetcode", "nums", "range", "repr", "staticmethod", "stderr", "stdin", "stdout", "str",
  "sys", "tuple", "utf", "vars", "zip",
]);


let spellCheckerPromise;


function loadSpellChecker() {
  if (!spellCheckerPromise) {
    spellCheckerPromise = Promise.all([
      fetch("/assets/en.aff").then((response) => response.text()),
      fetch("/assets/en.dic").then((response) => response.text()),
    ]).then(([aff, dic]) => nspell(aff, dic));
  }
  return spellCheckerPromise;
}


class BreakpointMarker extends GutterMarker {
  toDOM() {
    const marker = document.createElement("span");
    marker.className = "cm-breakpoint-dot";
    return marker;
  }
}


const breakpointMarker = new BreakpointMarker();


const breakpointState = StateField.define({
  create() {
    return Decoration.none;
  },
  update(markers, transaction) {
    markers = markers.map(transaction.changes);
    for (const effect of transaction.effects) {
      if (effect.is(toggleBreakpoint)) {
        let present = false;
        markers.between(effect.value, effect.value, () => { present = true; });
        markers = present ? markers.update({filter: (from) => from !== effect.value}) : markers.update({add: [breakpointMarker.range(effect.value)]});
      }
      if (effect.is(replaceBreakpoints)) {
        const builder = new RangeSetBuilder();
        for (const lineNumber of effect.value) {
          if (lineNumber >= 1 && lineNumber <= transaction.state.doc.lines) {
            builder.add(transaction.state.doc.line(lineNumber).from, transaction.state.doc.line(lineNumber).from, breakpointMarker);
          }
        }
        markers = builder.finish();
      }
    }
    return markers;
  },
});


const breakpointGutter = gutter({
  class: "cm-breakpoint-gutter",
  markers: (view) => view.state.field(breakpointState),
  domEventHandlers: {
    mousedown(view, line) {
      view.dispatch({effects: toggleBreakpoint.of(line.from)});
      return true;
    },
  },
});


const whitespaceDecoration = Decoration.mark({class: "cm-visible-spaces"});


function whitespaceRanges(view) {
  const builder = new RangeSetBuilder();
  for (const range of view.visibleRanges) {
    const text = view.state.doc.sliceString(range.from, range.to);
    const expression = / +/g;
    let match;
    while ((match = expression.exec(text)) !== null) {
      builder.add(range.from + match.index, range.from + match.index + match[0].length, whitespaceDecoration);
    }
  }
  return builder.finish();
}


const visibleWhitespace = ViewPlugin.fromClass(class {
  constructor(view) {
    this.decorations = whitespaceRanges(view);
  }
  update(update) {
    if (update.docChanged || update.viewportChanged) this.decorations = whitespaceRanges(update.view);
  }
}, {decorations: (plugin) => plugin.decorations});


const misspellingDecoration = Decoration.mark({
  class: "cm-spelling-error",
  attributes: {title: "Possible spelling mistake"},
});


function spellingParts(token, tokenStart) {
  const parts = [];
  const expression = /[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|_|$)/g;
  let match;
  while ((match = expression.exec(token)) !== null) {
    parts.push({word: match[0], from: tokenStart + match.index});
  }
  return parts;
}


function spellingRanges(view, checker) {
  const builder = new RangeSetBuilder();
  for (const range of view.visibleRanges) {
    const text = view.state.doc.sliceString(range.from, range.to);
    const expression = /[A-Za-z][A-Za-z_]*/g;
    let match;
    while ((match = expression.exec(text)) !== null) {
      for (const part of spellingParts(match[0], range.from + match.index)) {
        const normalized = part.word.toLowerCase();
        if (normalized.length <= 2 || SPELLING_EXCLUSIONS.has(normalized)) continue;
        if (part.word === part.word.toUpperCase() && part.word.length <= 4) continue;
        if (!checker.correct(normalized)) {
          builder.add(part.from, part.from + part.word.length, misspellingDecoration);
        }
      }
    }
  }
  return builder.finish();
}


const spellingCheck = ViewPlugin.fromClass(class {
  constructor(view) {
    this.checker = null;
    this.decorations = Decoration.none;
    loadSpellChecker()
      .then((checker) => {
        if (!view.destroyed) view.dispatch({effects: spellingReady.of(checker)});
      })
      .catch(() => {});
  }
  update(update) {
    for (const transaction of update.transactions) {
      for (const effect of transaction.effects) {
        if (effect.is(spellingReady)) this.checker = effect.value;
      }
    }
    if (this.checker && (update.docChanged || update.viewportChanged || update.transactions.some((transaction) => transaction.effects.some((effect) => effect.is(spellingReady))))) {
      this.decorations = spellingRanges(update.view, this.checker);
    }
  }
}, {decorations: (plugin) => plugin.decorations});


const currentLineEffect = StateEffect.define();
const currentLineState = StateField.define({
  create() {
    return Decoration.none;
  },
  update(value, transaction) {
    value = value.map(transaction.changes);
    for (const effect of transaction.effects) {
      if (effect.is(currentLineEffect)) {
        if (!effect.value) return Decoration.none;
        const line = transaction.state.doc.line(Math.min(effect.value, transaction.state.doc.lines));
        return Decoration.set([Decoration.line({class: "cm-diagnostic-line"}).range(line.from)]);
      }
    }
    return value;
  },
  provide: (field) => EditorView.decorations.from(field),
});


const editorTheme = EditorView.theme({
  "&": {backgroundColor: "#faf8ef", color: "#292d29"},
  ".cm-scroller": {
    fontFamily: '"JetBrains Mono", ui-monospace, SFMono-Regular, Consolas, monospace',
    fontSize: "15px",
    lineHeight: "1.6",
  },
  ".cm-content": {caretColor: "#567863"},
  ".cm-gutters": {backgroundColor: "#f2eedf", color: "#7b7b71", borderRight: "1px solid #ddd7c5"},
  ".cm-breakpoint-gutter": {cursor: "pointer"},
  ".cm-breakpoint-gutter .cm-gutterElement": {cursor: "pointer"},
  ".cm-activeLine": {backgroundColor: "#edf2e8"},
  ".cm-activeLineGutter": {backgroundColor: "#edf2e8"},
  "&.cm-focused .cm-cursor": {borderLeftColor: "#567863"},
}, {dark: false});


const pythonHighlightStyle = HighlightStyle.define([
  {tag: tags.comment, color: "#6f7d70", fontStyle: "italic"},
  {tag: tags.keyword, color: "#98533b", fontWeight: "600"},
  {tag: [tags.function(tags.variableName), tags.definition(tags.variableName)], color: "#4f7563"},
  {tag: [tags.className, tags.typeName], color: "#76638c"},
  {tag: [tags.string, tags.special(tags.string)], color: "#86732e"},
  {tag: [tags.number, tags.bool, tags.null], color: "#725d91"},
  {tag: tags.operator, color: "#9b6048"},
  {tag: tags.self, color: "#8a6d34"},
  {tag: tags.punctuation, color: "#555a54"},
]);


export function createPythonEditor(parent, options = {}) {
  const view = new EditorView({
    parent,
    state: EditorState.create({
      doc: options.value || "",
      extensions: [
        breakpointState,
        breakpointGutter,
        lineNumbers(),
        highlightActiveLineGutter(),
        highlightSpecialChars(),
        history(),
        drawSelection(),
        dropCursor(),
        highlightActiveLine(),
        currentLineState,
        visibleWhitespace,
        spellingCheck,
        python(),
        closeBrackets(),
        bracketMatching(),
        editorTheme,
        syntaxHighlighting(pythonHighlightStyle),
        EditorState.tabSize.of(4),
        indentUnit.of("    "),
        EditorView.contentAttributes.of({"aria-label": "Python source code", spellcheck: "false"}),
        keymap.of([indentWithTab, ...closeBracketsKeymap, ...defaultKeymap, ...historyKeymap]),
        EditorView.lineWrapping,
        EditorView.updateListener.of((update) => {
          if (update.docChanged && options.onChange) options.onChange(update.state.doc.toString());
        }),
      ],
    }),
  });

  return {
    getValue() {
      return view.state.doc.toString();
    },
    setValue(value) {
      view.dispatch({changes: {from: 0, to: view.state.doc.length, insert: value}});
    },
    getBreakpoints() {
      const lines = [];
      view.state.field(breakpointState).between(0, view.state.doc.length, (from) => lines.push(view.state.doc.lineAt(from).number));
      return lines.sort((left, right) => left - right);
    },
    clearBreakpoints() {
      view.dispatch({effects: replaceBreakpoints.of([])});
    },
    setCurrentLine(lineNumber) {
      view.dispatch({effects: currentLineEffect.of(lineNumber || null)});
    },
    focus() {
      view.focus();
    },
  };
}


window.createPythonEditor = createPythonEditor;
