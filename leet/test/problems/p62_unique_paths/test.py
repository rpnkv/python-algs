import pytest

from problems.p62_unique_paths.bruteforce_solution import Solution

TEST_CASES = [
    pytest.param((3, 7), 28, id="Example 1"),
    pytest.param((3, 2), 3, id="Example 2"),
    #pytest.param((1, 1), 2, id="My example 1"),
]


@pytest.mark.parametrize(["incoming_dimensions", "expected_outcome"], TEST_CASES)
def test(incoming_dimensions: tuple[int], expected_outcome):
    m, n = incoming_dimensions[0], incoming_dimensions[1]

    assert Solution().uniquePaths(m, n) == expected_outcome
