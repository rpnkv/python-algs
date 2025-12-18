import dataclasses
from typing import Optional

from common.tree_node import TreeNode


def traverse_recursive(root: Optional[TreeNode]) -> list[int]:
    """
    Ok, what's happen when this program executes for a tree like this: [2,1,3]?
    Iteration   Call stack contents
    1           [root=1]
    2           [root=2]

    """

    if root is None:
        return []
    else:
        return traverse_recursive(root.left) + [root.val] + traverse_recursive(root.right)


def traverse_iterative(root: Optional[TreeNode]) -> list[int]:
    @dataclasses.dataclass
    class TraversalLog:
        node: TreeNode
        left_visited = False
        right_visited = False

    nodes_stack = []
    result = []

    current_node = root
    node_popped = False

    while True:
        if current_node.left is None and current_node.right is None:
            pass

        if current_node.left is not None:
            nodes_stack.append(current_node)
            continue
        else:
            result.append(current_node.val)
            current_node = nodes_stack.pop()

    return result
