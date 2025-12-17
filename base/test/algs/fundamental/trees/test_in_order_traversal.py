from algs.fundamental.trees.in_order_traversal import traverse
from common.tree_node import TreeNode

def _init_test_tree() -> TreeNode:
    root = TreeNode(3)

    root.left=TreeNode(9)
    root.right=TreeNode(20)

    root_right = root.right

    root_right.left=TreeNode(15)
    root_right.right=TreeNode(7)

    return root



def test_parametrised():
    assert traverse(_init_test_tree()) == []