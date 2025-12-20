from common.tree_node import TreeNode


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
