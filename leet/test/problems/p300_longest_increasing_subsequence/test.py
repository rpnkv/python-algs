import pytest

from problems.p300_longest_increasing_subsequence.solution import Solution

TEST_CASES = [
    pytest.param([9, 1, 4, 2, 3, 3, 7], 4, id="Example 1"),
    pytest.param([0, 3, 1, 3, 2, 3], 4, id="Example 2"),
    pytest.param([1, 1], 1, id="My case 1"),
    pytest.param([1, 2], 2, id="My case 2"),
]


@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test(incoming: list[int], expected_outcome: int):
    assert Solution().lengthOfLIS(incoming) == expected_outcome
