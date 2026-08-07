import sys


def encode(strs: list[str]) -> str:
    # TODO: return a single encoded string
    pass


def decode(s: str) -> list[str]:
    # TODO: return the original list of strings
    pass


def main() -> None:
    # Format: count n, then per string a length line and the raw bytes
    buf = sys.stdin.buffer
    n = int(buf.readline())
    strs = []
    for _ in range(n):
        length = int(buf.readline())
        s = buf.read(length).decode()
        buf.read(1)  # newline separator
        strs.append(s)
    decoded = decode(encode(strs))
    out = [str(len(decoded))]
    for s in decoded:
        out.append(str(len(s)))
        out.append(s)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
