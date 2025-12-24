import pytest

from problems.easy.p27_remove_element.solution import Solution

sol = Solution()

TEST_VALUES = [
    pytest.param([], 5, 0, id="empty"),
    pytest.param([1], 2, 1, id="single non-equal"),
    pytest.param([1], 1, 0, id="single equal"),
    pytest.param([1, 2, 2, 3, 4], 2, 3, id="regular"),
]


@pytest.mark.parametrize(["nums", "value", "expected_output"], TEST_VALUES)
def test_solution(nums: list[int], value: int, expected_output: int):
    assert sol.removeElement(nums, value) == expected_output
