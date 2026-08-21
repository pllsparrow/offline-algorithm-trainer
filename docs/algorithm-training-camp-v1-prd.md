# Algorithm Training Camp V1 PRD

Status: Draft for implementation
Owner: Single local Mac user
Date: 2026-08-21

## Product Positioning

Algorithm Training Camp is a personal, offline, ACM-style Python practice system. It is the
local equivalent of a small LeetCode/NowCoder training site: the learner selects a problem,
writes a complete stdin/stdout program, debugs it in the browser, and submits it against a
reproducible local test set.

The system is independent from saveJob. V1 exposes a link from saveJob; it does not share
authentication, database tables, or runtime processes with saveJob.

## V1 Goals

- Make all 150 Hot 150 problems selectable by number without showing 150 items at once.
- Make ACM input, output, and sample data visible before coding.
- Let the learner edit and run Python 3.12 code in a browser.
- Provide a practical white-box debugger: breakpoints, pause, continue, step over, locals,
  call stack, and the line that raised an exception.
- Keep displayed debugging information concise and useful for learning.
- Run representative examples during normal practice and approximately 100 deterministic cases
  on submit, using fewer when the valid input domain is naturally small.
- Persist browser drafts and learning progress in the algorithm service's SQLite database.
- Write the submitted code back to `hot_150/` after the full test run completes.

## V1 User Flow

1. Start the algorithm service on localhost.
2. Enter a problem number or choose a filtered problem from the navigation.
3. Read the ACM format, NeetCode link, and separately maintained representative examples.
4. Edit the complete Python program in the browser. Changes are saved as a draft.
5. Run the selected representative examples or a custom stdin payload.
6. Add breakpoints and inspect the current line, locals, call stack, stdout, and errors.
7. Submit. The service stores a temporary submission, runs all fixed cases for the problem
   (normally around 100), writes the source to the problem file, and records the result.
8. Use the saveJob link to return to the personal learning/work workflow.

## V1 In Scope

- 150 problem metadata records, navigation, number jump, search/filter, and progress marker.
- Existing ACM problem files and judge integration.
- A separate examples dataset with 2-3 deliberately different cases per problem, including
  representative empty, boundary, duplicate, negative, or minimal inputs where applicable.
- Python 3.12 only.
- CodeMirror-style browser editor with line numbers, syntax highlighting, indentation, current
  line highlighting, and breakpoint markers. No code completion requirement.
- Sample run, custom-input run, single-case rerun, and full submit.
- White-box debugging described in the technical specification.
- Local SQLite drafts, submissions, and progress.
- Local-only execution with no network feature and no AI feature.

## V1 Out Of Scope

- Accounts, multi-user data, cloud execution, online judging, or public code execution.
- AI hints, generated solutions, community discussions, video lessons, or social features.
- C++, Java, Go, JavaScript, or any language besides Python 3.12.
- Full PyCharm features: code completion, refactoring, watch expressions, variable mutation,
  conditional breakpoints, step into third-party libraries, and multithread debugging.
- Embedding the debugger inside saveJob. V1 uses a link; iframe or reverse-proxy integration is
  a later decision.
- A stateful Notebook workspace. V1 keeps the main editor focused on clean-process ACM execution
  and PyCharm-style breakpoint debugging.

## Post-V1 Learning Notes

- Algorithm notes, code experiments, data-structure observations, and complexity checks use an
  executable Notebook format so code snippets can be edited and run beside the explanation.
- Markdown notes are reserved for text-first written-test and interview material such as
  experience summaries, communication patterns, company processes, and behavioral questions.
- The Notebook is a learning and experimentation surface, not a submission source. Formal
  submissions always use the complete `.py` program from the main editor and a clean process.
- A future lightweight data inspector may expose selected values or short experiments without
  sharing state with judge runs.

## Success Criteria

- A learner can jump to any of 150 problems and see its current source and ACM examples.
- A syntax/runtime error identifies the file line and shows a concise human-readable hint.
- A breakpoint on a loop exposes the changing locals without flooding the screen with every event.
- A successful submit runs the problem's complete deterministic case set and records an accepted
  result; the normal target is approximately 100 cases rather than an exact count.
- A failed submit preserves both the draft and the submitted source for inspection.
- saveJob can open the service through one documented localhost link.
