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

    if not root:
        return []
    else:
        return traverse_recursive(root.left) + [root.val] + traverse_recursive(root.right)


def traverse_recursive_pre_check(root: Optional[TreeNode]) -> list[int]:
    if root.left is not None:
        left = traverse_recursive_pre_check(root.left)
    else:
        left = []

    if root.right is not None:
        right = traverse_recursive_pre_check(root.right)
    else:
        right = []

    return left + [root.val] + right


def traverse_iterative_my_worse(root: Optional[TreeNode]) -> list[int]:
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

    raise RuntimeError("Unexpected state")


def traverse_iterative_pre_check(root: Optional[TreeNode]) -> list[int]:
    """
    If the node has left sibling, it 100% must be processed after it. We put current into stack and switch current to
    the left.

    If the node has no left, it just commits itself. And switches to the right.

    If node is stack-extracted, it commits itself.

    If the node was extracted from the stack, left and right values must be committed.
    If the node is entered for the first time, then it's value may be commited only when there is no left sibling.
    If left sibling exists, current node must be put in stack and switch to the left one.
    So, if node is extracted from the stack, that it does have a left sibling.

    """
    from typing import List
    stack: List[TreeNode] = []
    traversal: List[int] = []
    current_node: Optional[TreeNode] = root

    stack_extracted = False

    while True:
        if stack_extracted:
            stack_extracted = False

            traversal.append(current_node.left.val)
            traversal.append(current_node.val)

            current_node = current_node.right
        else:
            if not current_node:
                if not stack:
                    return traversal
                else:
                    current_node = stack.pop()
                    stack_extracted = True
            else:
                if not current_node.left:
                    stack_extracted = True
                else:
                    stack.append(current_node)
                    current_node = current_node.left

    return traversal
