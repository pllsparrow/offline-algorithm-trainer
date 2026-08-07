import sys


class TimeMap:
    def __init__(self) -> None:
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass

OPS = {
        'TimeMap': ([], None),
        'set': (['str', 'str', 'int'], None),
        'get': (['str', 'int'], 'str'),
    }


def main() -> None:
    # Format: first line q (operations), then q lines of 'op args...'. Output: one result per operation (null for void; space-separated values for lists)
    data = sys.stdin.buffer.read().split()
    p = 0
    q = int(data[p]); p += 1
    obj = None
    out = []
    for _ in range(q):
        op = data[p].decode(); p += 1
        arg_types = OPS[op][0]
        args = []
        for t in arg_types:
            if t == 'int':
                args.append(int(data[p])); p += 1
            elif t == 'float':
                args.append(float(data[p])); p += 1
            elif t == 'str':
                args.append(data[p].decode()); p += 1
            elif t == 'list[int]':
                m = int(data[p]); p += 1
                args.append(list(map(int, data[p:p + m]))); p += m
        if op == 'TimeMap':
            obj = TimeMap(*args)
            out.append('null')
        else:
            res = getattr(obj, op)(*args)
            if res is None:
                out.append('null')
            elif isinstance(res, bool):
                out.append('1' if res else '0')
            elif isinstance(res, list):
                out.append(' '.join(map(str, res)))
            else:
                out.append(str(res))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
