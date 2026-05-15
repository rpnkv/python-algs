import pytest

from algs.fundamental.trees.traversal.dfs.preorder_recursive import traverse
from algs.fundamental.trees.traversal.dfs.preorder_test_cases import TEST_CASES
from common.tree_node import TreeNode


@pytest.mark.parametrize(["nodes_list", "expected_outcome"], TEST_CASES)
def test(nodes_list: list[int], expected_outcome: list[int]):
    tree = TreeNode.from_level_order_array(nodes_list)
    assert traverse(tree) == expected_outcome