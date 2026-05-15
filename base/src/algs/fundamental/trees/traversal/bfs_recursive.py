from common.tree_node import TreeNode


def traverse(*roots: TreeNode) -> list[int]:
    level_values = []
    children = []

    has_value = False
    for root in roots:
        if root and not has_value:
            has_value = True

        curr_children = [None, None]
        if root:
            level_values.append(root.val)
            curr_children[0] = root.left
            curr_children[1] = root.right
        else:
            level_values.append(None)

        children += curr_children


    if not has_value:
        return []
    else:
        return  level_values + traverse(*children)

