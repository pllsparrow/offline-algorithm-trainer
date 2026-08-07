from __future__ import annotations

from support import GraphNode, ListNode, Node, RandomNode, TreeNode


class TimeMap:
    def __init__(self) -> None:
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass


from acm_support import run_operations


if __name__ == "__main__":
    run_operations(TimeMap)
