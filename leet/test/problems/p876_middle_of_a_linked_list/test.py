from typing import Optional

import pytest

from common.list_node import ListNode
from problems.p876_middle_of_a_linked_list.solution import Solution

TEST_CASES = [
    pytest.param([], None, id="Empty list"),
    pytest.param([1], 1, id="Single node list"),
    pytest.param([1, 2], 2, id="Two nodes list"),
    pytest.param([1, 2, 3], 2, id="Three nodes list"),
]

@pytest.mark.parametrize(["input_as_array", "expected_answer_value"], TEST_CASES)
def test(input_as_array: list[int], expected_answer_value: Optional[int]):
    expected_answer = None if expected_answer_value is None else ListNode(expected_answer_value)
    actual_answer = Solution().middleNode(ListNode.to_linked_list(input_as_array))

    if actual_answer:
        actual_answer.next = None

    assert expected_answer == actual_answer
