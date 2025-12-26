import pytest

from algs.fundamental.trees.in_order_traversal import traverse_recursive, traverse_iterative_my_worse, \
    traverse_iterative_pre_check
from common.tree_node import TreeNode


def _init_test_tree() -> TreeNode:
    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root_right = root.right

    root_right.left = TreeNode(15)
    root_right.right = TreeNode(7)

    return root


TEST_CASES = [
    pytest.param([1, 2, 3], [2, 1, 3], id="very basic case"),
    pytest.param(_init_test_tree().to_level_order_array(), [9, 3, 15, 20, 7], id="one more my case"),
    pytest.param([1, None, 2, None, None, 3, None], [1, 3, 2], id="example 1"),
]


@pytest.mark.parametrize(["traversing_tree_as_array", "expected_values"], TEST_CASES)
def test_recursive(traversing_tree_as_array, expected_values):
    root = TreeNode.from_level_order_array(traversing_tree_as_array)
    assert traverse_recursive(root) == expected_values


@pytest.mark.parametrize(["traversing_tree_as_array", "expected_values"], TEST_CASES)
def test_recursive_pre_check(traversing_tree_as_array, expected_values):
    root = TreeNode.from_level_order_array(traversing_tree_as_array)
    assert traverse_recursive(root) == expected_values


@pytest.mark.parametrize(["traversing_tree_as_array", "expected_values"], TEST_CASES)
def test_traverse_iterative_my_worse(traversing_tree_as_array, expected_values):
    root = TreeNode.from_level_order_array(traversing_tree_as_array)
    assert traverse_iterative_my_worse(root) == expected_values


THOROUGH_TESTS = [
    pytest.param([], [], id="empty tree"),
    pytest.param([1, None, None], [1], id="root only"),
]


@pytest.mark.parametrize(["traversing_tree_as_array", "expected_values"], THOROUGH_TESTS)
def test_traverse_iterative_pre_check(traversing_tree_as_array, expected_values):
    root = TreeNode.from_level_order_array(traversing_tree_as_array)
    assert traverse_iterative_pre_check(root) == expected_values
