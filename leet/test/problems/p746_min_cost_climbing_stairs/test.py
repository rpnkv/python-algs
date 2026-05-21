import pytest

from problems.p746_min_cost_climbing_stairs.solution import Solution
from problems.p746_min_cost_climbing_stairs.solution_iterative import Solution as SolutionIterative

TEST_CASES = [
    pytest.param([1, 5, 2, 4], 3, id="My case"),
    pytest.param([10, 15, 20], 15, id="Example 1"),
    pytest.param([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6, id="Example 2"),
]


@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test(incoming: list[int], expected_outcome: int):
    assert Solution().minCostClimbingStairs(incoming) == expected_outcome


@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test_iterative(incoming: list[int], expected_outcome: int):
    assert SolutionIterative().minCostClimbingStairs(incoming) == expected_outcome