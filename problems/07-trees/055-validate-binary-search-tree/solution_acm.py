from __future__ import annotations

from support import GraphNode, ListNode, Node, RandomNode, TreeNode


class Solution:
    @classmethod
    def validate(cls, node: TreeNode[int] | None, min_val: float, max_val: float) -> bool:
        pass

    def is_valid_bst(self, root: TreeNode[int] | None) -> bool:
        pass


from acm_support import run_solution


if __name__ == "__main__":
    run_solution(Solution, 'validate', ['TreeNode'])
