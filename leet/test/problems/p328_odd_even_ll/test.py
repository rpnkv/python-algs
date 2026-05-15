import pytest

from common.list_node import ListNode
from problems.p328_odd_even_ll.solution import Solution

TEST_CASES = [
    pytest.param([], [], id="Empty"),
    pytest.param([1], [1], id="1 node"),
    pytest.param([1, 2], [1, 2], id="2 nodes"),
    pytest.param([1, 2, 3], [1, 3, 2], id="3 nodes"),
    pytest.param([1, 2, 3, 4], [1, 3, 2, 4], id="4 nodes"),
]


@pytest.mark.parametrize(["incoming_list", "expected_outcome"], TEST_CASES)
def test(incoming_list: list[int], expected_outcome: list[int]):
    assert Solution().oddEvenList(ListNode.to_linked_list(incoming_list)) == ListNode.to_linked_list(expected_outcome)
