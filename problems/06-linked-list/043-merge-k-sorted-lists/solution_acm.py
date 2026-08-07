from __future__ import annotations

from support import GraphNode, ListNode, Node, RandomNode, TreeNode


class Solution:
    def merge_k_lists(self, lists: list[ListNode[int] | None]) -> ListNode[int] | None:
        pass

    def _divide_conquer(self, lists: list[ListNode[int] | None], left: int, right: int) -> ListNode[int] | None:
        pass

    def _merge_two(self, l1: ListNode[int] | None, l2: ListNode[int] | None) -> ListNode[int] | None:
        pass


from acm_support import run_solution


if __name__ == "__main__":
    run_solution(Solution, 'merge_k_lists', ['List[ListNode]'])
