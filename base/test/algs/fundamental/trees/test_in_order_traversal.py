import pytest

from algs.fundamental.trees.in_order_traversal import traverse
from common.tree_node import TreeNode


def _init_test_tree() -> TreeNode:
    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root_right = root.right

    root_right.left = TreeNode(15)
    root_right.right = TreeNode(7)

    return root


@pytest.mark.parametrize(
    argnames=["traversing_tree_as_array", "expected_values"],
    argvalues=[
        # ([1, None, 2, None, None, 3], [1, 3, 2])
        ([1, 2, 3], [2, 1, 3])
    ],
    ids=["example 1"]
)
def test_parametrised(traversing_tree_as_array, expected_values):
    root = TreeNode.froThm_level_order_array(traversing_tree_as_array)
    assert traverse(root) == expected_values
