import pytest

TEST_CASES = [
    pytest.param([9, 1, 4, 2, 3, 3, 7], 4, id="Example 1"),
    pytest.param([0, 3, 1, 3, 2, 3], 4, id="Example 2"),
    pytest.param([1, 1], 1, id="My case 1"),
    pytest.param([1, 2], 2, id="My case 2"),
]


@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test_bruteforce(incoming: list[int], expected_outcome: int):
    from problems.p300_longest_increasing_subsequence.bruteforce_solution import Solution
    assert Solution().lengthOfLIS(incoming) == expected_outcome

@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test_bottom_up_dp(incoming: list[int], expected_outcome: int):
    from problems.p300_longest_increasing_subsequence.bruteforce_solution import Solution
    assert Solution().lengthOfLIS(incoming) == expected_outcome