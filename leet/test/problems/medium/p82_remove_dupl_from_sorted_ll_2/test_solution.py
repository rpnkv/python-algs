import pytest

from common.list_node import ListNode
from problems.medium.p82_remove_dupl_from_sorted_ll_2.iterative_solution import Solution as IterativeSolution

TEST_CASES = [
    pytest.param([], []),
    pytest.param([1], [1]),
    pytest.param([1, 1], []),
    pytest.param([1, 1, 2], [2, ]),
    pytest.param([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
]

sol = IterativeSolution()


@pytest.mark.parametrize(["input_list", "expected_output_list"], TEST_CASES)
def test_solution(input_list, expected_output_list):
    input_head = ListNode.to_linked_list(input_list)
    expected_output_head = ListNode.to_linked_list(expected_output_list)

    assert sol.deleteDuplicates(input_head) == expected_output_head
