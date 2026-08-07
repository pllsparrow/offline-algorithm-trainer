from __future__ import annotations

from support import GraphNode, ListNode, Node, RandomNode, TreeNode


class Codec:
    def __init__(self) -> None:
        pass

    def serialize(self, root: TreeNode[int] | None) -> str:
        pass

    def deserialize(self, data: str) -> TreeNode[int] | None:
        pass


from acm_support import run_solution


if __name__ == "__main__":
    run_solution(Solution, 'serialize', ['TreeNode'])
