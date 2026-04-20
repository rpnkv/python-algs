import pytest

from problems.p485_max_consecutive_ones.solution import Solution

TEST_CASES = [
    pytest.param([1, 1, 0, 1, 1, 1], 3, id="Example 1"),
    pytest.param([1, 0, 1, 1, 0, 1], 2, id="Example 2"),
]


@pytest.mark.parametrize(["nums", "expected_answer"], TEST_CASES)
def test(nums: list[int], expected_answer: int):
    assert Solution().findMaxConsecutiveOnes(nums) == expected_answer
