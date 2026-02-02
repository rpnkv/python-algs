import pytest

from problems.p27_remove_element.naive_solution import Solution

sol = Solution()

TEST_CASES = [
    pytest.param([], 0, [], id="empty input"),
    pytest.param([2, 2], 2, [], id="empty result"),
    pytest.param([3, 2, 2], 3, [2, 2], id="removed from beginning"),
    pytest.param([3, 3, 2, 2], 3, [2, 2], id="removed two from beginning"),
    pytest.param([2, 2, 3], 3, [2, 2], id="removed from ending"),
    pytest.param([2, 2, 3, 3], 3, [2, 2], id="removed two from ending"),
    pytest.param([3, 2, 2, 3], 3, [2, 2], id="base case"),
]


@pytest.mark.parametrize(["nums", "val", "expected_output"], TEST_CASES)
def test(nums, val, expected_output):
    lngth = sol.removeElement(nums, val)
    assert nums[:lngth] == expected_output
