from common.tree_node import TreeNode


def traverse(root: TreeNode) -> list[int]:
    stack = []
    res = []

    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            res.append(root.val)
            root = root.right

    return res
