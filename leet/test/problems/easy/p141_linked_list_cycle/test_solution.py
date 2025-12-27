from typing import Optional

import pytest

from common.list_node import ListNode
from problems.easy.p141_linked_list_cycle.solution import Solution

sol = Solution()

TEST_VALUES = [
    pytest.param(None, False, id="empty"),
]


@pytest.mark.parametrize(
    ["head", "expected_status"], TEST_VALUES
)
def test(head: Optional[ListNode], expected_status: bool):
    assert sol.hasCycle(head) == expected_status
