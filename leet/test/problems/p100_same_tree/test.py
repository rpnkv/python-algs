import pytest

from common.tree_node import TreeNode
from problems.p100_same_tree.solution_recursive import Solution

TEST_CASES = [
    pytest.param([1, 2, 3], [1, 2, 3], True, id="Example 1")
]


@pytest.mark.parametrize(["p_list", "q_list", "expected_answer"], TEST_CASES)
def test_recursive(p_list: list[int], q_list: list[int], expected_answer: bool):
    p = TreeNode.from_level_order_array(p_list)
    q = TreeNode.from_level_order_array(q_list)
    assert Solution().compare(p, q) == expected_answer
