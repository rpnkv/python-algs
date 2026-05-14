import pytest

from algs.fundamental.trees.traversal.bfs_iterative import traverse
from bfs_test_cases import TEST_CASES
from common.tree_node import TreeNode


@pytest.mark.parametrize(["incoming_list", "expected_outcome"], TEST_CASES)
def test(incoming_list: list[int], expected_outcome: list[int]):
    incoming = TreeNode.from_level_order_array(incoming_list)
    assert traverse(incoming) == expected_outcome