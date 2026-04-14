import pytest

from common.tree_node import TreeNode
from problems.p1161_maximum_level_sum_binary_tree.solution import Solution

TEST_CASES = [
    pytest.param([1, 7, 0, 7, -8, None, None], 2, id="Example 1")
]

@pytest.mark.parametrize(["tree_as_list", "expected_answer"], TEST_CASES)
def test(tree_as_list: list[int], expected_answer: int):
    root = TreeNode.from_level_order_array(tree_as_list)

    assert Solution().maxLevelSum(root) == expected_answer