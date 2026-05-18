import pytest

from problems.p746_min_cost_climbing_stairs.solution import Solution

TEST_CASES = [
    pytest.param([10, 15, 20], 15, id="Example 1"),
    pytest.param([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6, id="Example 2"),
]


@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test(incoming: list[int], expected_outcome: int):
    assert Solution().minCostClimbingStairs(incoming) == expected_outcome
