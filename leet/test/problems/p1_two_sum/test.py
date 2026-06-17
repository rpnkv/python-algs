import pytest

from problems.p1_two_sum.solution import Solution

TEST_CASES = [
    (pytest.param([2, 7, 11, 15], 9, [1, 2], id="Example 1")),
    (pytest.param([2, 3, 4], 6, [1, 3], id="Example 2")),
    (pytest.param([-1, 0], 1, [1, 2], id="Example 3"))
]


@pytest.mark.parametrize(["incoming", "target", "expected_outcome"], TEST_CASES)
def test(incoming: list[int], target: int, expected_outcome: list[int]):
    sol = Solution()

    assert sol.twoSum(incoming, target) == expected_outcome
