from typing import Optional

import pytest

# from common.list_node import ListNode
from problems.p141_linked_list_cycle.expected_solution import Solution, ListNode

sol = Solution()


def looped_list_odd_elements() -> ListNode:
    head = ListNode(2)
    tail = ListNode(15)

    middle = ListNode(4)
    middle2 = ListNode(5)
    middle.next = middle2

    head.next = middle
    middle2.next = tail

    tail.next = head
    return head


def looped_list_even_elements() -> ListNode:
    head = ListNode(2)
    tail = ListNode(15)

    middle = ListNode(5)
    middle2 = ListNode(6)
    middle3 = ListNode(7)

    head.next = middle
    middle.next = middle2
    middle2.next = middle3

    middle3.next = tail

    tail.next = head

    return head


TEST_VALUES = [
    pytest.param(None, False, id="empty"),
    pytest.param(ListNode(), False, id="1 element"),
    pytest.param(ListNode.to_linked_list([2, 3]), False, id="2 elements"),
    pytest.param(ListNode.to_linked_list([2, 3, 4]), False, id="3 elements"),
    pytest.param(looped_list_odd_elements(), True, id="looped odd"),
    pytest.param(looped_list_even_elements(), True, id="looped even"),
]


@pytest.mark.parametrize(
    ["head", "expected_status"], TEST_VALUES
)
def test(head: Optional[ListNode], expected_status: bool):
    assert sol.hasCycle(head) == expected_status
