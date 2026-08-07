from __future__ import annotations

from support import GraphNode, ListNode, Node, RandomNode, TreeNode


class Node:
    def __init__(self, x: int, next: Node | None=None, random: Node | None=None):
        pass


from acm_support import run_solution


if __name__ == "__main__":
    run_solution(Solution, 'solve', ['RandomNode'])
