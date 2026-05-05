import pytest

from common.list_node import ListNode
from problems.p2130_max_twin_sum_ll.solution import Solution

TEST_CASES = [
    pytest.param([1, 2], 3, id="My case 1"),
    pytest.param([1, 2, 3, 4], 5, id="My case 2"),
    pytest.param([1, 2, 5, 3, 4, 2], 8, id="My case 3"),
]

@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test(incoming: list[int], expected_outcome: int):
    incoming_list = ListNode.to_linked_list(incoming)
    assert Solution().pairSum(incoming_list) == expected_outcome