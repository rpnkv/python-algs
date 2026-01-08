import pytest

from problems.easy.p27_remove_element.naive_solution import Solution

sol = Solution()

TEST_CASES = [
    pytest.param([3, 2, 2, 3], 3, [2, 2], id="base case")
]


@pytest.mark.parametrize(["nums", "val", "expected_output"], TEST_CASES)
def test(nums, val, expected_output):
    lngth = sol.removeElement(nums, val)
    assert nums[:lngth] == expected_output
