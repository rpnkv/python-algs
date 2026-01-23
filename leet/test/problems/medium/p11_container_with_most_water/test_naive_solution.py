import pytest

from problems.medium.p11_container_with_most_water.naive_solution import Solution

sol = Solution()


@pytest.mark.parametrize(
    argnames=["heights", "expected_square"],
    argvalues=[
        ([1, 3, 1, 4], 6),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ]
)
def test(heights, expected_square):
    assert sol.maxArea(heights) == expected_square
