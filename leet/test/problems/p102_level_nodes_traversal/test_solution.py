import pytest

from common.tree_node import TreeNode
from problems.p102_level_order_traversal.solution import Solution

sol = Solution()

TEST_CASES = [
    pytest.param([3,9,20,None,None,15,7], [[3],[9,20],[15,7]], id="Example 1"),
    pytest.param([1], [[1]], id="Example 2"),
    pytest.param([], [], id="Example 3"),
]

@pytest.mark.parametrize(["incoming_tree", "expected_outcome"], TEST_CASES)
def test(incoming_tree: list[int], expected_outcome:list[list[int]]):
    assert Solution().levelOrder(TreeNode.from_leetcode_array(incoming_tree)) == expected_outcome