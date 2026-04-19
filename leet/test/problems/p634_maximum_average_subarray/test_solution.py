import pytest

from problems.p634_maximum_average_subarray.solution import Solution

TEST_CASES = [
    pytest.param([1, 12, -5, -6, 50, 3], 4, 12.75, id="case 1"),
    pytest.param([4, 2, 1, 3, 3], 2, 3, id="case 22"),
]


@pytest.mark.parametrize(["nums", "k", "expected_answer"], TEST_CASES)
def test(nums: list[int], k: int, expected_answer: float):
    assert Solution().findMaxAverage(nums, k) == expected_answer
