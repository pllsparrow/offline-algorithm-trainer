#!/usr/bin/env python3
"""Build ACM (stdin/stdout) specs for every problem from the function-mode dataset.

All 150 problems are converted to a pure text protocol: each solution runs as an
independent process that reads stdin and writes stdout. There is no LeetCode-style
class adapter left. Output for problems with multiple valid answers is canonicalised
(sorted), so the judge can keep using exact whitespace-normalised text comparison.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def dump_json(value) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


# ---------------------------------------------------------------------------
# Classification sets
# ---------------------------------------------------------------------------

# Inputs whose list[list[int]] argument is a rectangular grid (read as rows x cols).
MATRIX_INT_SLUGS = {
    "max-area-of-island",
    "rotting-oranges",
    "walls-and-gates",
    "pacific-atlantic-water-flow",
    "swim-in-rising-water",
    "longest-increasing-path-in-a-matrix",
    "rotate-image",
    "set-matrix-zeroes",
    "spiral-matrix",
    "search-a-2d-matrix",
}

# Outputs whose list[list[int]] result is a rectangular grid.
MATRIX_OUTPUT_SLUGS = {
    "walls-and-gates",
    "rotate-image",
    "set-matrix-zeroes",
}

# Single string inputs that may contain spaces (read the whole line).
STR_LINE_SLUGS = {
    "valid-palindrome",
    "longest-substring-without-repeating-characters",
}

# Orderless outputs: the judge requires a canonical (sorted) print order.
NESTED_ORDERLESS = {
    "group-anagrams",
    "3sum",
    "subsets",
    "subsets-ii",
    "permutations",
    "combination-sum",
    "combination-sum-ii",
    "palindrome-partitioning",
    "k-closest-points-to-origin",
    "pacific-atlantic-water-flow",
}
FLAT_ORDERLESS = {
    "top-k-frequent-elements",
    "partition-labels",
    "letter-combinations-of-a-phone-number",
    "word-search-ii",
    "generate-parentheses",
}

# Operation-based design problems.
OPS_SPEC = {
    "min-stack": {
        "class": "MinStack",
        "ops": {
            "MinStack": ([], None),
            "push": (["int"], None),
            "pop": ([], None),
            "top": ([], "int"),
            "getMin": ([], "int"),
        },
    },
    "time-based-key-value-store": {
        "class": "TimeMap",
        "ops": {
            "TimeMap": ([], None),
            "set": (["str", "str", "int"], None),
            "get": (["str", "int"], "str"),
        },
    },
    "lru-cache": {
        "class": "LRUCache",
        "ops": {
            "LRUCache": (["int"], None),
            "put": (["int", "int"], None),
            "get": (["int"], "int"),
        },
    },
    "kth-largest-element-in-a-stream": {
        "class": "KthLargest",
        "ops": {
            "KthLargest": (["int", "list[int]"], None),
            "add": (["int"], "int"),
        },
    },
    "design-twitter": {
        "class": "Twitter",
        "ops": {
            "Twitter": ([], None),
            "postTweet": (["int", "int"], None),
            "getNewsFeed": (["int"], "list[int]"),
            "follow": (["int", "int"], None),
            "unfollow": (["int", "int"], None),
        },
    },
    "find-median-from-data-stream": {
        "class": "MedianFinder",
        "ops": {
            "MedianFinder": ([], None),
            "addNum": (["int"], None),
            "findMedian": ([], "float"),
        },
    },
    "implement-trie-prefix-tree": {
        "class": "Trie",
        "ops": {
            "Trie": ([], None),
            "insert": (["str"], None),
            "search": (["str"], "bool"),
            "startsWith": (["str"], "bool"),
        },
    },
    "design-add-and-search-words-data-structure": {
        "class": "WordDictionary",
        "ops": {
            "WordDictionary": ([], None),
            "addWord": (["str"], None),
            "search": (["str"], "bool"),
        },
    },
    "detect-squares": {
        "class": "DetectSquares",
        "ops": {
            "DetectSquares": ([], None),
            "add": (["list[int]"], None),
            "count": (["list[int]"], "int"),
        },
    },
}


# ---------------------------------------------------------------------------
# Input schema inference
# ---------------------------------------------------------------------------

def infer_schema(slug: str, param_type: str, value) -> str:
    if param_type == "ListNode":
        return "listnode"
    if param_type == "List[ListNode]":
        return "listlistnode"
    if param_type == "TreeNode":
        return "tree"
    if param_type == "TreeNodeValue":
        return "treeval"
    if param_type == "GraphNode":
        return "graphadj"
    if param_type == "RandomNode":
        return "randomnode"
    # plain parameter (param_type == "")
    if isinstance(value, bool):
        return "int"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        return "str_line" if slug in STR_LINE_SLUGS else "str"
    if isinstance(value, list):
        if not value:
            return "ints"
        if all(isinstance(x, int) for x in value):
            return "ints"
        if all(isinstance(x, str) for x in value):
            return "strs_lenpref" if slug == "encode-and-decode-strings" else "strs"
        if all(isinstance(x, list) for x in value):
            flat = [item for row in value for item in row]
            if flat and all(isinstance(item, str) for item in flat):
                if all(len(item) == 1 for item in flat):
                    return "board_str"
                return "strpairs"
            if slug in MATRIX_INT_SLUGS:
                return "matrix_int"
            width = len(value[0]) if value else 2
            return f"edges{width}"
    return "int"


# ---------------------------------------------------------------------------
# Input serialisation
# ---------------------------------------------------------------------------

def ser_input(schema: str, value) -> str:
    if schema == "int":
        return f"{value}\n"
    if schema == "float":
        return f"{value}\n"
    if schema in ("str", "str_line", "treeval"):
        return f"{value}\n"
    if schema == "ints" or schema == "listnode":
        return f"{len(value)}\n" + " ".join(map(str, value)) + "\n"
    if schema == "strs":
        return f"{len(value)}\n" + "".join(f"{x}\n" for x in value)
    if schema == "strs_lenpref":
        parts = [str(len(value))]
        for s in value:
            parts.append(str(len(s)))
            parts.append(s)
        return "\n".join(parts) + "\n"
    if schema.startswith("edges"):
        return f"{len(value)}\n" + "".join(" ".join(map(str, row)) + "\n" for row in value)
    if schema == "strpairs":
        return f"{len(value)}\n" + "".join(" ".join(row) + "\n" for row in value)
    if schema == "matrix_int":
        r, c = len(value), len(value[0]) if value else 0
        return f"{r} {c}\n" + "".join(" ".join(map(str, row)) + "\n" for row in value)
    if schema == "board_str":
        r, c = len(value), len(value[0]) if value else 0
        return f"{r} {c}\n" + "".join(" ".join(row) + "\n" for row in value)
    if schema == "tree":
        toks = " ".join("null" if x is None else str(x) for x in value)
        return f"{len(value)}\n{toks}\n"
    if schema == "listlistnode":
        out = [str(len(value))]
        for lst in value:
            out.append(str(len(lst)))
            out.append(" ".join(map(str, lst)))
        return "\n".join(out) + "\n"
    if schema == "graphadj":
        out = [str(len(value))]
        for nbrs in value:
            out.append(str(len(nbrs)) + ("" if not nbrs else " " + " ".join(map(str, nbrs))))
        return "\n".join(out) + "\n"
    if schema == "randomnode":
        out = [str(len(value))]
        for val, idx in value:
            out.append(f"{val} {-1 if idx is None else idx}")
        return "\n".join(out) + "\n"
    raise ValueError(f"unknown input schema {schema}")


# ---------------------------------------------------------------------------
# Output serialisation (with canonicalisation)
# ---------------------------------------------------------------------------

def ser_output(slug: str, value) -> str:
    if slug == "encode-and-decode-strings":
        parts = [str(len(value))]
        for s in value:
            parts.append(str(len(s)))
            parts.append(s)
        return "\n".join(parts) + "\n"
    if slug == "n-queens":
        if not value:
            return "0\n"
        boards = sorted(value)
        out = [str(len(boards))]
        for board in boards:
            out.extend(board)
        return "\n".join(out) + "\n"
    if value is None:
        return ""
    if isinstance(value, bool):
        return "1\n" if value else "0\n"
    if isinstance(value, int):
        return f"{value}\n"
    if isinstance(value, float):
        return f"{value}\n"
    if isinstance(value, str):
        return value + "\n"
    if isinstance(value, list):
        if not value:
            return ""
        if slug in NESTED_ORDERLESS:
            groups = sorted([sorted(g) for g in value])
            return "\n".join(" ".join(map(str, g)) for g in groups) + "\n"
        if slug in FLAT_ORDERLESS:
            vals = sorted(value)
            return " ".join(map(str, vals)) + "\n"
        if any(x is None for x in value):
            return " ".join("null" if x is None else str(x) for x in value) + "\n"
        if all(isinstance(x, (int, float)) for x in value):
            return " ".join(map(str, value)) + "\n"
        if all(isinstance(x, str) for x in value):
            return " ".join(value) + "\n"
        if all(isinstance(x, list) for x in value):
            if slug in MATRIX_OUTPUT_SLUGS:
                r, c = len(value), len(value[0]) if value else 0
                return f"{r} {c}\n" + "".join(" ".join(map(str, row)) + "\n" for row in value)
            if slug == "clone-graph":
                out = [str(len(value))]
                for nbrs in value:
                    out.append(str(len(nbrs)) + ("" if not nbrs else " " + " ".join(map(str, nbrs))))
                return "\n".join(out) + "\n"
            if slug == "copy-list-with-random-pointer":
                out = [str(len(value))]
                for val, idx in value:
                    out.append(f"{val} {-1 if idx is None else idx}")
                return "\n".join(out) + "\n"
            if all(isinstance(row, list) and row and all(isinstance(item, str) for item in row) for row in value):
                r, c = len(value), len(value[0]) if value else 0
                return f"{r} {c}\n" + "".join(" ".join(row) + "\n" for row in value)
            return f"{len(value)}\n" + "".join(" ".join(map(str, row)) + "\n" for row in value)
    return str(value) + "\n"


# ---------------------------------------------------------------------------
# OPS serialisation
# ---------------------------------------------------------------------------

def ser_ops_arg(value) -> str:
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return str(value)
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return f"{len(value)} " + " ".join(map(str, value)) if value else "0"
    return str(value)


def ser_ops_out(value) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, list):
        return " ".join(map(str, value))
    return str(value)


def ser_ops_case(case: dict) -> str:
    ops = case["ops"]
    args = case["args"]
    lines = [str(len(ops))]
    for op, op_args in zip(ops, args):
        if op_args:
            lines.append(op + " " + " ".join(ser_ops_arg(a) for a in op_args))
        else:
            lines.append(op)
    stdin = "\n".join(lines) + "\n"
    stdout = "\n".join(ser_ops_out(v) for v in case["expected"]) + "\n"
    return stdin, stdout


# ---------------------------------------------------------------------------
# Format descriptions
# ---------------------------------------------------------------------------

def describe_input(schema: str) -> str:
    return {
        "int": "an integer",
        "float": "a float",
        "str": "a string token",
        "str_line": "a whole input line (may contain spaces)",
        "treeval": "a tree node value (integer)",
        "ints": "an integer list: count n then n integers",
        "listnode": "a linked list: count n then n integers",
        "strs": "a string list: count n then n tokens",
        "strs_lenpref": "strings with length prefix: count n, then per string a length line and the raw bytes",
        "matrix_int": "an integer matrix: rows r, cols c, then r lines of c integers",
        "board_str": "a char board: rows r, cols c, then r lines of c chars",
        "strpairs": "string pairs: count m then m lines of two tokens",
        "tree": "a binary tree: count n then n level-order values (null for missing)",
        "listlistnode": "k linked lists: count k, then per list count n and n integers",
        "graphadj": "a graph: count n, then per node degree d and d neighbour ids",
        "randomnode": "a random list: count n, then n lines of value and random-index (-1 for null)",
    }.get(schema, f"{schema}: count then values")


def describe_output(slug: str, expected) -> str:
    if slug in OPS_SPEC:
        return "one result per operation (null for void; space-separated values for lists)"
    if slug == "encode-and-decode-strings":
        return "count n, then per string a length line and the raw bytes (round-trip of the input)"
    if slug == "n-queens":
        return "the solution count S, then S boards each as n lines of Q/."
    if expected is None or (isinstance(expected, list) and not expected):
        return "print nothing"
    if isinstance(expected, bool):
        return "1 if true else 0"
    if isinstance(expected, int):
        return "the integer"
    if isinstance(expected, float):
        return "the float"
    if isinstance(expected, str):
        return "the string"
    if isinstance(expected, list):
        if any(x is None for x in expected):
            return "level-order values space-separated (null for missing)"
        if slug in NESTED_ORDERLESS:
            return "each group on its own line (sorted; each group sorted)"
        if slug in FLAT_ORDERLESS:
            return "the values space-separated in ascending order"
        if all(isinstance(x, (int, float)) for x in expected):
            return "the values space-separated"
        if all(isinstance(x, str) for x in expected):
            return "the strings space-separated"
        if all(isinstance(x, list) for x in expected):
            if slug in MATRIX_OUTPUT_SLUGS:
                return "the matrix: rows r, cols c, then r lines of c integers"
            if slug == "clone-graph":
                return "count n then n neighbour lists (degree then ids)"
            if slug == "copy-list-with-random-pointer":
                return "count n then n lines of value and random-index (-1 for null)"
            return "count m then m lines of pairs"
    return "the answer"


# ---------------------------------------------------------------------------
# Starter generation
# ---------------------------------------------------------------------------

def token_starter(format_desc: str, schemas: list[str]) -> str:
    parse_lines = ["    data = sys.stdin.buffer.read().split()", "    p = 0"]
    names = []
    for i, schema in enumerate(schemas):
        name = f"v{i}"
        names.append(name)
        parse_lines.append(ops_parse_line(schema, name))
    body = "\n".join(parse_lines)
    refs = ", ".join(names)
    return (
        "import sys\n\n\n"
        "def main() -> None:\n"
        f"    # Format: {format_desc}\n"
        f"{body}\n"
        f"    # TODO: compute the answer from {refs} and print it\n\n\n"
        'if __name__ == "__main__":\n'
        "    main()\n"
    )


def ops_parse_line(schema: str, name: str) -> str:
    if schema == "int":
        return f"    {name} = int(data[p]); p += 1"
    if schema == "float":
        return f"    {name} = float(data[p]); p += 1"
    if schema in ("str", "treeval"):
        return f"    {name} = data[p].decode(); p += 1"
    if schema in ("ints", "listnode"):
        return (
            f"    n_{name} = int(data[p]); p += 1\n"
            f"    {name} = list(map(int, data[p:p + n_{name}])); p += n_{name}"
        )
    if schema == "strs":
        return (
            f"    n_{name} = int(data[p]); p += 1\n"
            f"    {name} = [data[p + j].decode() for j in range(n_{name})]; p += n_{name}"
        )
    if schema.startswith("edges"):
        w = int(schema[5:])
        return (
            f"    m_{name} = int(data[p]); p += 1\n"
            f"    {name} = [[int(data[p + w * i + j]) for j in range({w})] for i in range(m_{name})]; p += {w} * m_{name}"
        )
    if schema == "strpairs":
        return (
            f"    m_{name} = int(data[p]); p += 1\n"
            f"    {name} = [[data[p + 2 * i].decode(), data[p + 2 * i + 1].decode()] for i in range(m_{name})]; p += 2 * m_{name}"
        )
    if schema == "matrix_int":
        return (
            f"    r_{name} = int(data[p]); c_{name} = int(data[p + 1]); p += 2\n"
            f"    {name} = [list(map(int, data[p + i * c_{name}:p + (i + 1) * c_{name}])) for i in range(r_{name})]; p += r_{name} * c_{name}"
        )
    if schema == "board_str":
        return (
            f"    r_{name} = int(data[p]); c_{name} = int(data[p + 1]); p += 2\n"
            f"    {name} = [[data[p + i * c_{name} + j].decode() for j in range(c_{name})] for i in range(r_{name})]; p += r_{name} * c_{name}"
        )
    if schema == "tree":
        return (
            f"    n_{name} = int(data[p]); p += 1\n"
            f"    {name} = [None if data[p + i] == b'null' else int(data[p + i]) for i in range(n_{name})]; p += n_{name}"
        )
    if schema == "listlistnode":
        return (
            f"    k_{name} = int(data[p]); p += 1\n"
            f"    {name} = []\n"
            f"    for _ in range(k_{name}):\n"
            f"        n_{name} = int(data[p]); p += 1\n"
            f"        {name}.append(list(map(int, data[p:p + n_{name}]))); p += n_{name}"
        )
    if schema == "graphadj":
        return (
            f"    n_{name} = int(data[p]); p += 1\n"
            f"    {name} = []\n"
            f"    for _ in range(n_{name}):\n"
            f"        d_{name} = int(data[p]); p += 1\n"
            f"        {name}.append(list(map(int, data[p:p + d_{name}]))); p += d_{name}"
        )
    if schema == "randomnode":
        return (
            f"    n_{name} = int(data[p]); p += 1\n"
            f"    {name} = []\n"
            f"    for _ in range(n_{name}):\n"
            f"        val = int(data[p]); idx = int(data[p + 1]); p += 2\n"
            f"        {name}.append([val, None if idx == -1 else idx])"
        )
    return f"    {name} = data[p]; p += 1  # TODO parse {schema}"


def str_line_starter(format_desc: str) -> str:
    return (
        "import sys\n\n\n"
        "def main() -> None:\n"
        f"    # Format: {format_desc}\n"
        '    s = sys.stdin.readline().rstrip("\\n")\n'
        "    # TODO: compute the answer and print it\n\n\n"
        'if __name__ == "__main__":\n'
        "    main()\n"
    )


def encode_starter() -> str:
    return (
        "import sys\n\n\n"
        "def encode(strs: list[str]) -> str:\n"
        "    # TODO: return a single encoded string\n"
        "    pass\n\n\n"
        "def decode(s: str) -> list[str]:\n"
        "    # TODO: return the original list of strings\n"
        "    pass\n\n\n"
        "def main() -> None:\n"
        "    # Format: count n, then per string a length line and the raw bytes\n"
        "    buf = sys.stdin.buffer\n"
        "    n = int(buf.readline())\n"
        "    strs = []\n"
        "    for _ in range(n):\n"
        "        length = int(buf.readline())\n"
        "        s = buf.read(length).decode()\n"
        "        buf.read(1)  # newline separator\n"
        "        strs.append(s)\n"
        "    decoded = decode(encode(strs))\n"
        "    out = [str(len(decoded))]\n"
        "    for s in decoded:\n"
        "        out.append(str(len(s)))\n"
        "        out.append(s)\n"
        '    sys.stdout.write("\\n".join(out) + "\\n")\n\n\n'
        'if __name__ == "__main__":\n'
        "    main()\n"
    )


def ops_starter(slug: str, format_desc: str) -> str:
    spec = OPS_SPEC[slug]
    cls = spec["class"]
    class_block = extract_class_block(slug, cls)
    ops_repr = render_ops_spec(spec["ops"])
    return (
        "import sys\n\n\n"
        f"{class_block}\n"
        f"OPS = {ops_repr}\n\n\n"
        "def main() -> None:\n"
        f"    # Format: {format_desc}\n"
        "    data = sys.stdin.buffer.read().split()\n"
        "    p = 0\n"
        "    q = int(data[p]); p += 1\n"
        f"    obj = None\n"
        "    out = []\n"
        "    for _ in range(q):\n"
        "        op = data[p].decode(); p += 1\n"
        "        arg_types = OPS[op][0]\n"
        "        args = []\n"
        "        for t in arg_types:\n"
        "            if t == 'int':\n"
        "                args.append(int(data[p])); p += 1\n"
        "            elif t == 'float':\n"
        "                args.append(float(data[p])); p += 1\n"
        "            elif t == 'str':\n"
        "                args.append(data[p].decode()); p += 1\n"
        "            elif t == 'list[int]':\n"
        "                m = int(data[p]); p += 1\n"
        "                args.append(list(map(int, data[p:p + m]))); p += m\n"
        f"        if op == '{cls}':\n"
        f"            obj = {cls}(*args)\n"
        "            out.append('null')\n"
        "        else:\n"
        "            res = getattr(obj, op)(*args)\n"
        "            if res is None:\n"
        "                out.append('null')\n"
        "            elif isinstance(res, bool):\n"
        "                out.append('1' if res else '0')\n"
        "            elif isinstance(res, list):\n"
        "                out.append(' '.join(map(str, res)))\n"
        "            else:\n"
        "                out.append(str(res))\n"
        '    sys.stdout.write("\\n".join(out) + "\\n")\n\n\n'
        'if __name__ == "__main__":\n'
        "    main()\n"
    )


def extract_class_block(slug: str, cls: str) -> str:
    problems = load_json(DATA / "problems.json")
    starter = next(p["starter"] for p in problems if p["slug"] == slug)
    lines = starter.splitlines()
    keep = []
    started = False
    for line in lines:
        if not started:
            if line.startswith("class "):
                started = True
                keep.append(line)
            continue
        keep.append(line)
    return "\n".join(keep).rstrip() + "\n"


def render_ops_spec(ops: dict) -> str:
    items = []
    for op, (arg_types, ret) in ops.items():
        items.append(f"        {op!r}: ({arg_types!r}, {ret!r})")
    return "{\n" + ",\n".join(items) + ",\n    }"


def make_starter(slug: str, schemas: list[str], format_desc: str) -> str:
    if slug in OPS_SPEC:
        return ops_starter(slug, format_desc)
    if slug == "encode-and-decode-strings":
        return encode_starter()
    if schemas == ["str_line"]:
        return str_line_starter(format_desc)
    return token_starter(format_desc, schemas)


# ---------------------------------------------------------------------------
# Spec building
# ---------------------------------------------------------------------------

def build_spec(problem: dict, test_spec: dict) -> dict:
    slug = problem["slug"]
    if test_spec["method"] == "__ops__":
        cases = []
        for case in test_spec["cases"]:
            stdin, stdout = ser_ops_case(case)
            cases.append({"stdin": stdin, "stdout": stdout})
        format_desc = "first line q (operations), then q lines of 'op args...'. Output: " + describe_output(slug, None)
        return {
            "protocol": "text",
            "format": format_desc,
            "starter": ops_starter(slug, format_desc),
            "cases": cases,
        }

    param_types = test_spec.get("param_types", [])
    first_case = test_spec["cases"][0]
    args = first_case.get("args", [])
    schemas = [infer_schema(slug, param_types[i] if i < len(param_types) else "", value)
               for i, value in enumerate(args)]

    cases = []
    for case in test_spec["cases"]:
        stdin_parts = [ser_input(schemas[i], value)
                       for i, value in enumerate(case.get("args", []))]
        stdin = "".join(stdin_parts)
        stdout = ser_output(slug, case["expected"])
        cases.append({"stdin": stdin, "stdout": stdout})

    in_desc = "; ".join(f"arg{i+1}: {describe_input(s)}" for i, s in enumerate(schemas))
    out_desc = describe_output(slug, first_case["expected"])
    format_desc = f"Input: {in_desc}. Output: {out_desc}."
    return {
        "protocol": "text",
        "format": format_desc,
        "starter": make_starter(slug, schemas, format_desc),
        "cases": cases,
    }


def build_specs(problems: list[dict], tests: dict) -> dict:
    output = {}
    for problem in problems:
        slug = problem["slug"]
        output[slug] = build_spec(problem, tests[slug])
    return output


def solution_path(problem: dict) -> Path:
    return ROOT / problem["path"] / "solution_acm.py"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build ACM text specs for all problems")
    parser.add_argument("--check", action="store_true", help="Fail when generated specs differ from acm_tests.json")
    parser.add_argument("--write-solutions", action="store_true", help="Create missing solution_acm.py starters")
    parser.add_argument("--force", action="store_true", help="With --write-solutions, overwrite all starters")
    parser.add_argument("--debug-schemas", action="store_true", help="Print inferred input schemas per slug")
    args = parser.parse_args()

    problems = load_json(DATA / "problems.json")
    tests = load_json(DATA / "tests.json")
    specs = build_specs(problems, tests)

    if args.debug_schemas:
        for problem in problems:
            slug = problem["slug"]
            t = tests[slug]
            if t["method"] == "__ops__":
                print(f"{slug:<48} OPS")
                continue
            pt = t.get("param_types", [])
            first = t["cases"][0]
            schemas = [infer_schema(slug, pt[i] if i < len(pt) else "", v)
                       for i, v in enumerate(first.get("args", []))]
            print(f"{slug:<48} {schemas}")
        return

    generated = dump_json(specs)
    output_path = DATA / "acm_tests.json"

    if args.check:
        current = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
        if current != generated:
            raise SystemExit("ACM specs are stale; run scripts/build_acm.py")
        print(f"ACM specs up to date: {len(problems)} problems")
        return

    output_path.write_text(generated, encoding="utf-8")

    if args.write_solutions:
        created = 0
        overwritten = 0
        for problem in problems:
            path = solution_path(problem)
            path.parent.mkdir(parents=True, exist_ok=True)
            if path.exists() and not args.force:
                continue
            existed = path.exists()
            path.write_text(specs[problem["slug"]]["starter"], encoding="utf-8")
            if existed:
                overwritten += 1
            else:
                created += 1
        print(f"ACM solution starters: {created} created, {overwritten} overwritten")

    print(f"ACM specs ready: {len(problems)} problems")


if __name__ == "__main__":
    main()
