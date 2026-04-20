import pytest

from problems.p1493_longest_subarray_of_ones.solution_bruteforce import Solution

TEST_CASES = [
    pytest.param([0], 0, id="My case 1"),
    pytest.param([0], 0, id="My case 2"),
    pytest.param([0, 1], 1, id="My case 3"),
    pytest.param([1, 0], 1, id="My case 4"),
    pytest.param([1, 1, 1], 2, id="My case 5"),
    pytest.param([1, 1, 0], 2, id="My case 6"),
    pytest.param([1, 0, 1], 2, id="My case 7"),
    pytest.param([1, 0, 1, 1], 3, id="My case 8"),

    pytest.param([1, 1, 0, 1], 3, id="Example 1"),
    pytest.param([0, 1, 1, 1, 0, 1, 1, 0, 1], 5, id="Example 2"),
    pytest.param([1, 1, 1], 2, id="Example 3"),
]


@pytest.mark.parametrize(["nums", "expected"], TEST_CASES)
def test(nums: list[int], expected: int) -> None:
    assert Solution().longestSubarray(nums) == expected
