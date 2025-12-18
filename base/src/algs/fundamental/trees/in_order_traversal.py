from typing import Optional

from common.tree_node import TreeNode


def traverse_recursive(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    else:
        return traverse_recursive(root.left) + [root.val] + traverse_recursive(root.right)

def traverse_iterative(root: Optional[TreeNode]) -> list[int]:
    nodes_stack = []
    result = []


