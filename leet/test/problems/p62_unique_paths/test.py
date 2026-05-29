import pytest

TEST_CASES = [
    pytest.param((3, 7), 28, id="Example 1"),
    pytest.param((3, 2), 3, id="Example 2"),
    #pytest.param((1, 1), 2, id="My example 1"),
]


@pytest.mark.parametrize(["incoming_dimensions", "expected_outcome"], TEST_CASES)
def test_bruteforce(incoming_dimensions: tuple[int], expected_outcome):
    from problems.p62_unique_paths.bruteforce_solution import Solution
    m, n = incoming_dimensions[0], incoming_dimensions[1]

    assert Solution().uniquePaths(m, n) == expected_outcome


@pytest.mark.parametrize(["incoming_dimensions", "expected_outcome"], TEST_CASES)
def test_bottom_up_dp(incoming_dimensions: tuple[int], expected_outcome):
    from problems.p62_unique_paths.bottom_up_dp_solution import Solution
    m, n = incoming_dimensions[0], incoming_dimensions[1]

    assert Solution().uniquePaths(m, n) == expected_outcome
