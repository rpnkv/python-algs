from common.tree_node import TreeNode


def traverse(root: TreeNode) -> list[int]:
    if not root:
        return []
    else:
        return traverse(root.left) + [root.val] + traverse(root.right)