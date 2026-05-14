from common.tree_node import TreeNode


def traverse(root: TreeNode) -> list[int]:
    current = [root] if root else []
    children = []
    res = []

    while any([current_node for current_node in current]):
        for node in current:
            l_r = (None, None)
            if node:
                res.append(node.val)
                l_r=(node.left, node.right)
            else:
                res.append(None)

            children += [*l_r]

        current = children
        children = []

    return res