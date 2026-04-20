import pytest

from problems.p1004_max_consecutive_nums.solution import Solution

sol = Solution()

TEST_CASES = [
    #pytest.param([], 0, 0, id="empty input"),
    pytest.param([1, 1, 1, 1], 0, 4, id="only 4 '1'"),
    pytest.param([1, 0, 0, 1], 3, 4, id="zeroes lesser than allowed"),
    pytest.param([0, 0], 0, 0, id="zeroes lesser than allowed"),
    pytest.param([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6, id="example 1"),
    pytest.param([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10, id="example 2"),
]


@pytest.mark.parametrize(["nums", "k", "expected_max"], TEST_CASES)
def test(nums: list[int], k: int, expected_max: int):
    assert sol.longestOnes(nums, k) == expected_max
