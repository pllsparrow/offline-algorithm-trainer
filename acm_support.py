from __future__ import annotations

import json
import re
import sys
from collections import deque
from typing import Any

from support import GraphNode, ListNode, Node, RandomNode, TreeNode


def list_to_linked(values: list[Any] | None) -> ListNode | None:
    dummy = ListNode()
    current = dummy
    for value in values or []:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def list_to_tree(values: list[Any] | None) -> TreeNode | None:
    if not values or values[0] is None:
        return None
    nodes = [None if value is None else TreeNode(value) for value in values]
    children = deque(nodes[1:])
    for node in nodes:
        if node is None:
            continue
        if children:
            node.left = children.popleft()
        if children:
            node.right = children.popleft()
    return nodes[0]


def find_tree_node(root: TreeNode | None, value: Any) -> TreeNode | None:
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            continue
        if node.val == value:
            return node
        queue.append(node.left)
        queue.append(node.right)
    return None


def adj_to_graph(adjacency: list[list[int]] | None) -> GraphNode | None:
    if not adjacency:
        return None
    nodes = {index + 1: Node(index + 1) for index in range(len(adjacency))}
    for index, neighbors in enumerate(adjacency, start=1):
        nodes[index].neighbors = [nodes[value] for value in neighbors]
    return nodes[1]


def list_to_random_list(values: list[list[int | None]] | None) -> RandomNode | None:
    if not values:
        return None
    nodes = [Node(item[0]) for item in values]
    for index, item in enumerate(values):
        if index + 1 < len(nodes):
            nodes[index].next = nodes[index + 1]
        if item[1] is not None:
            nodes[index].random = nodes[item[1]]
    return nodes[0]


def convert_args(values: list[Any], param_types: list[str]) -> list[Any]:
    converted = []
    first_tree = None
    for index, value in enumerate(values):
        type_name = param_types[index] if index < len(param_types) else ""
        if type_name == "ListNode":
            converted.append(list_to_linked(value))
        elif type_name == "List[ListNode]":
            converted.append([list_to_linked(item) for item in value])
        elif type_name == "TreeNode":
            tree = list_to_tree(value)
            if first_tree is None:
                first_tree = tree
            converted.append(tree)
        elif type_name == "TreeNodeValue":
            converted.append(find_tree_node(first_tree, value))
        elif type_name == "GraphNode":
            converted.append(adj_to_graph(value))
        elif type_name == "RandomNode":
            converted.append(list_to_random_list(value))
        else:
            converted.append(value)
    return converted


def graph_to_adj(node: GraphNode | None) -> list[list[int]]:
    if node is None:
        return []
    seen = {}
    queue = deque([node])
    while queue:
        current = queue.popleft()
        if current.val in seen:
            continue
        seen[current.val] = current
        queue.extend(neighbor for neighbor in current.neighbors if neighbor.val not in seen)
    return [[neighbor.val for neighbor in seen[index].neighbors] for index in sorted(seen)]


def random_list_to_list(head: RandomNode | None) -> list[list[int | None]]:
    nodes = []
    positions = {}
    current = head
    while current:
        positions[id(current)] = len(nodes)
        nodes.append(current)
        current = current.next
    return [
        [node.val, None if node.random is None else positions.get(id(node.random))]
        for node in nodes
    ]


def normalize(value: Any) -> Any:
    if isinstance(value, TreeNode):
        output = []
        queue = deque([value])
        while queue:
            node = queue.popleft()
            if node is None:
                output.append(None)
                continue
            output.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        while output and output[-1] is None:
            output.pop()
        return output
    if isinstance(value, ListNode):
        output = []
        seen = set()
        while value and id(value) not in seen:
            seen.add(id(value))
            output.append(value.val)
            value = value.next
        return output
    if isinstance(value, Node):
        if value.neighbors:
            return graph_to_adj(value)
        return random_list_to_list(value)
    if isinstance(value, dict):
        return {key: normalize(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalize(item) for item in value]
    if isinstance(value, set):
        return sorted(normalize(item) for item in value)
    return value


def write_json(value: Any) -> None:
    json.dump(normalize(value), sys.stdout, ensure_ascii=False, separators=(",", ":"))
    sys.stdout.write("\n")


def camel_to_snake(value: str) -> str:
    first_pass = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", first_pass).lower()


def run_solution(solution_class: type, method_name: str, param_types: list[str]) -> None:
    args = json.load(sys.stdin)
    if not isinstance(args, list):
        raise ValueError("JSON ACM input must be a positional-argument array")
    instance = solution_class()
    result = getattr(instance, method_name)(*convert_args(args, param_types))
    write_json(result)


def run_operations(target_class: type) -> None:
    payload = json.load(sys.stdin)
    operations = payload["ops"]
    arguments = payload["args"]
    instance = None
    output = []
    for operation, args in zip(operations, arguments):
        if operation == target_class.__name__:
            instance = target_class(*args)
            output.append(None)
        else:
            method = getattr(instance, operation, None)
            if method is None:
                method = getattr(instance, camel_to_snake(operation))
            output.append(method(*args))
    write_json(output)
