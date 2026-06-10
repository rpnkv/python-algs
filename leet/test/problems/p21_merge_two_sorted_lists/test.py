import pytest

from common.list_node import ListNode
from problems.p21_merge_two_sorted_lists.merge_two_sorted_lists import Solution

TEST_CASES = [
    pytest.param([1, 2, 4], [1, 3, 5], [1, 1, 2, 3, 4, 5], id="Example 1"),
    pytest.param([], [1, 3, 5], [1, 3, 5], id="Example 2"),
    pytest.param([1, 3, 5], [], [1, 3, 5], id="Example 2 mirrored"),
    pytest.param([], [], [], id="Example 3"),
]


@pytest.mark.parametrize(["incoming1", "incoming2", "expected_outcome"], TEST_CASES)
def test(incoming1: list[int], incoming2: list[int], expected_outcome: list[int]):
    assert Solution().mergeTwoLists(
        ListNode.to_linked_list(incoming1),
        ListNode.to_linked_list(incoming2),
    ) == ListNode.to_linked_list(expected_outcome)