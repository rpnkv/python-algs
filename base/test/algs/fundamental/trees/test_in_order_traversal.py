import pytest

from algs.fundamental.trees.in_order_traversal import traverse_recursive, traverse_iterative
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
        ([1, 2, 3], [2, 1, 3]),
        (_init_test_tree().to_level_order_array(), [9, 3, 15, 20, 7]),
        ([1, None, 2, None, None, 3, None], [1, 3, 2]),
    ],
    ids=["very basic case", "one more my case","example 1", ]
)
def test_recursive(traversing_tree_as_array, expected_values):
    root = TreeNode.from_level_order_array(traversing_tree_as_array)
    assert traverse_recursive(root) == expected_values


@pytest.mark.parametrize(
    argnames=["traversing_tree_as_array", "expected_values"],
    argvalues=[
        ([1, 2, 3], [2, 1, 3]),
        (_init_test_tree().to_level_order_array(), [9, 3, 15, 20, 7]),
        ([1, None, 2, None, None, 3, None], [1, 3, 2]),
    ],
    ids=["very basic case", "one more my case","example 1", ]
)
def test_iterative(traversing_tree_as_array, expected_values):
    root = TreeNode.from_level_order_array(traversing_tree_as_array)
    assert traverse_iterative(root) == expected_values
