from typing import Optional

from common.tree_node import TreeNode


def are_equal(l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
    if not l and not r:
        return True

    if not l or not r:
        return False

    if l.val != r.val:
        return False

    return are_equal(l.left, r.left) and are_equal(l.right, r.right)


def is_valid(root: Optional[TreeNode], floor=float("-inf"), ceil=float("inf")) -> bool:
    if root is None:
        return True

    if root.left is not None and (root.left.val >= root.val or root.left.val <= floor):
        return False

    if root.right is not None and (root.right.val <= root.val or root.right.val >= ceil):
        return False

    return (
            is_valid(root.left, floor=floor, ceil=min(root.val, ceil))
            and
            is_valid(root.right, floor=max(root.val, floor), ceil=ceil)
    )


def get_tree_sum(root: TreeNode) -> int:
    if not root:
        return 0
    else:
        return root.val + get_tree_sum(root.left) + get_tree_sum(root.right)


def get_tree_depth_recursive(root: TreeNode) -> int:
    if not root:
        return 0
    else:
        return 1 + max(get_tree_depth_recursive(root.left), get_tree_depth_recursive(root.right))


def get_tree_depth_iterative(root: TreeNode) -> int:
    if root is None:
        return 0

    stack = []
    current = root
    sum = 0

    while stack:
        if stack[-1].left is not None:
            stack.append(root.left)
            continue

        if stack[-1].right is not None:
            stack.append(root.right)
            continue

        node = stack.pop()
        sum += node.val

    return sum
