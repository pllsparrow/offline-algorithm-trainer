from __future__ import annotations

from typing import Generic, TypeVar, cast


T = TypeVar("T")


class ListNode(Generic[T]):
    def __init__(self, val: T = cast(T, 0), next: "ListNode[T] | None" = None):
        self.val = val
        self.next = next


class TreeNode(Generic[T]):
    def __init__(
        self,
        val: T = cast(T, 0),
        left: "TreeNode[T] | None" = None,
        right: "TreeNode[T] | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val: int = 0, next=None, random=None, neighbors=None):
        if isinstance(next, list) and neighbors is None:
            neighbors = next
            next = None
        self.val = val
        self.next = next
        self.random = random
        self.neighbors = neighbors if neighbors is not None else []


GraphNode = Node
RandomNode = Node
