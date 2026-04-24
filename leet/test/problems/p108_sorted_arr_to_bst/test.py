import pytest

from common.tree_node import TreeNode
from problems.reverse_integer import Solution

TEST_CASES = [
    #pytest.param([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5], id="Example 1"),
    pytest.param([1, 3], [3, 1, None], id="Example 2"),
]


@pytest.mark.parametrize(["input_level_order", "output_tree"])
def test(input_level_order: list[int], output_tree: TreeNode):
    assert Solution
