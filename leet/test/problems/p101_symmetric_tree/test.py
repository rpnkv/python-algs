import pytest

from common.tree_node import TreeNode
from problems.p101_symmetric_tree.solution import Solution

TEST_CASES = [
    pytest.param([1, 2, 2, 3, 4, 4, 3], True, id="Example 1"),
    pytest.param([1, 2, 2, None, 3, None, 3], False, id="Example 2"),
]


@pytest.mark.parametrize(["tree_as_list", "expected_result"], TEST_CASES)
def test(tree_as_list: list[int], expected_result: bool):
    assert Solution().isSymmetric(TreeNode.from_level_order_array(tree_as_list)) == expected_result