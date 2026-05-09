import pytest

from common.tree_node import TreeNode
from problems.p1448_count_good_nodes_in_bt.solution import Solution

TEST_CASES = [
    pytest.param([3, 1, 4, 3, None, 1, 5], 4, id="Example 1"),
    pytest.param([3, 3, None, 4, 2], 3, id="Example 2"),
    pytest.param([1], 1, id="Example 3"),
]

@pytest.mark.parametrize(["incoming_list", "expected_outcome"], TEST_CASES)
def test(incoming_list: list[int], expected_outcome: int):
    assert Solution().goodNodes(TreeNode.from_leetcode_array(incoming_list)) == expected_outcome