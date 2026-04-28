import pytest

from common.tree_node import TreeNode

TEST_CASES = [
    pytest.param([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5], id="Example 1"),
    pytest.param([1, 3], [3, 1, None], id="Example 2"),
    #pytest.param([1, 2, 3], [2, 1, 3], id="My 1"),
    pytest.param([1], [1], id="My 1"),
    pytest.param([1, 2], [1, 2], id="My 2"),
]


@pytest.mark.parametrize(["input_sorted", "output_level_order"], TEST_CASES)
def test_my_solution(input_sorted: list[int], output_level_order: list[int]):
    from problems.p108_sorted_arr_to_bst.my_solution import Solution

    result = Solution().sortedArrayToBST(input_sorted)
    expected_result = TreeNode.from_leetcode_array(output_level_order)

    assert result == expected_result



@pytest.mark.parametrize(["input_sorted", "output_level_order"], TEST_CASES)
def test_solution(input_sorted: list[int], output_level_order: list[int]):
    from problems.p108_sorted_arr_to_bst.solution import Solution
    result = Solution().sortedArrayToBST(input_sorted)
    expected_result = TreeNode.from_leetcode_array(output_level_order)

    assert result == expected_result