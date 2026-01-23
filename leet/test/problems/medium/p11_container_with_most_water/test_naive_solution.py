import pytest

from problems.medium.p11_container_with_most_water.naive_solution import Solution
from problems.medium.p11_container_with_most_water.expected_solution import Solution as Solution_expected

TEST_CASES = [
    pytest.param([1, 3, 1, 4], 6, id="basic case"),
    pytest.param([1, 8, 6, 2, 5, 4, 8, 3, 7], 49, id="example case"),
]


@pytest.mark.parametrize(["heights", "expected_square"], TEST_CASES)
def test_naive(heights, expected_square):
    sol = Solution()
    assert sol.maxArea(heights) == expected_square


def test_expected(heights, expected_square):
    sol = Solution_expected()
