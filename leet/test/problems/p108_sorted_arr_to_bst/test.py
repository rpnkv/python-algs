import pytest

from common.tree_node import TreeNode

TEST_CASES = [
    pytest.param([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5], id="Example 1"),
    pytest.param([1, 3, None], [3, 1, None], id="Example 2"),
    pytest.param([1, 2, 3], [1, 2, 3], id="My 1"),
]


@pytest.mark.parametrize(["input_sorted", "output_level_order"], TEST_CASES)
def test_my_solution(input_sorted: list[int], output_level_order: list[int]):
    from problems.p108_sorted_arr_to_bst.solution import Solution
    # assert (
    #         Solution().sortedArrayToBST(input_sorted) ==
    #         TreeNode.from_level_order_array(output_level_order)
    # )



@pytest.mark.parametrize(["input_sorted", "output_level_order"], TEST_CASES)
def test_solution(input_sorted: list[int], output_level_order: list[int]):
    from problems.p108_sorted_arr_to_bst.my_solution import Solution
    assert (
            Solution().sortedArrayToBST(input_sorted) ==
            TreeNode.from_level_order_array(output_level_order)
    )
    #res = Solution().sortedArrayToBST(input_sorted)
    #print(res)