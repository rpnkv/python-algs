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
    if root is None:
        return []

    stack = []
    current = root
    nodes_ordered = []

    while True:
        if not current:
            if len(stack) == 0:
                return nodes_ordered
            else:
                current = stack.pop()
                nodes_ordered.append(current.val)
                if current.right is not None:
                    current = current.right
                else:
                    current = None
                continue

        if current.left is not None:
            stack.append(current)
            current = current.left
            continue
        else:
            if current.right is not None:
                nodes_ordered.append(current.val)
                current = current.right
            else:
                nodes_ordered.append(current.val)
                current = None
