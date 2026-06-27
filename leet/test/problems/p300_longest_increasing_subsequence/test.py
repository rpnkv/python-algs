import pytest

TEST_CASES = [
    pytest.param([9, 1, 4, 2, 3, 3, 7], 4, id="Example 1"),
    pytest.param([0, 3, 1, 3, 2, 3], 4, id="Example 2"),
    pytest.param([4, 10, 4, 3, 8, 9], 3, id="Case 16"),
    pytest.param([0, 1, 0, 3, 2, 3], 4, id="Case 4"),
    pytest.param([1, 1], 1, id="My case 1"),
    pytest.param([1, 2], 2, id="My case 2"),
    pytest.param([1, 1, 1], 1, id="My case 3"),
    pytest.param([1, 1, 2], 2, id="My case 4"),
    pytest.param([1, 2, 3], 3, id="My case 5"),
    pytest.param([1, 2, 1, 3], 3, id="My case 6"),
    pytest.param([4, 3, 8, 9], 3, id="My case 7"),
]


@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test_bruteforce(incoming: list[int], expected_outcome: int):
    from problems.p300_longest_increasing_subsequence.bruteforce_solution_not_working import Solution
    assert Solution().lengthOfLIS(incoming) == expected_outcome


@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test_recursive(incoming: list[int], expected_outcome: int):
    from problems.p300_longest_increasing_subsequence.recursive import Solution
    assert Solution().lengthOfLIS(incoming) == expected_outcome


@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test_bottom_up_dp(incoming: list[int], expected_outcome: int):
    from problems.p300_longest_increasing_subsequence.bottom_up_dp_solution import Solution
    assert Solution().lengthOfLIS(incoming) == expected_outcome


@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test_greedy(incoming: list[int], expected_outcome: int):
    from problems.p300_longest_increasing_subsequence.greedy_solution import Solution
    assert Solution().lengthOfLIS(incoming) == expected_outcome


