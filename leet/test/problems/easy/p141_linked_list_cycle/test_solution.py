from typing import Optional

import pytest

from common.list_node import ListNode
from problems.easy.p141_linked_list_cycle.solution import Solution

sol = Solution()

TEST_VALUES = [
    pytest.param(None, False, id="empty"),
    pytest.param(ListNode(), False, id="1 element"),
    pytest.param(ListNode.to_linked_list([2, 3]), False, id="2 elements"),
    pytest.param(ListNode.to_linked_list([2, 3, 4]), False, id="3 elements"),
    pytest.param(ListNode.to_linked_list([2, 3, 3, 5]), False, id="4 elements"),
]


@pytest.mark.parametrize(
    ["head", "expected_status"], TEST_VALUES
)
def test(head: Optional[ListNode], expected_status: bool):
    assert sol.hasCycle(head) == expected_status
