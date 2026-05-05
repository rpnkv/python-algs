import pytest

from common.list_node import ListNode
from problems.p206_reverse_linked_list.solution import Solution

TEST_CASES = [
    pytest.param([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], id="Example1"),
    pytest.param([1, 2], [2, 1], id="Example2"),
]


@pytest.mark.parametrize(
    ["incoming", "expected_outcome"], TEST_CASES
)
def test(incoming: list[int], expected_outcome: list[int]):
    incoming_list = ListNode.to_linked_list(incoming)
    expected_outcome_list = ListNode.to_linked_list(expected_outcome)
    assert Solution().reverseList(incoming_list) == expected_outcome_list
