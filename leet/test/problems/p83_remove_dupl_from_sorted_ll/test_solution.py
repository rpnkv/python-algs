import pytest

from common.list_node import ListNode
from problems.p83_remove_dupl_from_sorted_ll.solution import Solution

sol = Solution()


@pytest.mark.parametrize(
    argnames=["input_list", "expected_output_list"],
    argvalues=[
        ([1], [1]),
        ([1, 1], [1]),
        ([1, 1, 1], [1]),
        ([1, 1, 1, 2], [1, 2]),
        ([1, 2, 2], [1, 2]),
        ([1, 2, 2, 2], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
    ]
)
def test_solution(input_list, expected_output_list):
    input_head = ListNode.to_linked_list(input_list)
    expected_output_head = ListNode.to_linked_list(expected_output_list)

    assert sol.deleteDuplicates(input_head) == expected_output_head
