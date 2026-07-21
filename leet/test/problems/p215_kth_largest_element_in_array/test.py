import pytest
from typing import List

from problems.p215_kth_largest_element_in_array.solution_oldest import Solution

TEST_CASES = [
    pytest.param([*range(0, 6)], 3, 3, id="My case 1"),
    pytest.param([3, 2, 1, 5, 6, 4], 2, 5, id="Example 1"),
    pytest.param([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4, id="Example 2"),
]


@pytest.mark.parametrize(["incoming_list","k", "expected_outcome"], TEST_CASES)
def test(incoming_list: List[int], k: int, expected_outcome: int):
    assert Solution().findKthLargest(incoming_list, k) == expected_outcome