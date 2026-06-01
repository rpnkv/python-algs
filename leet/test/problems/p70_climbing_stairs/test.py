import pytest

from problems.p70_climbing_stairs.solution_recursive_mem import Solution as SolutionRecursiveMem
from problems.p70_climbing_stairs.solution_recursive import Solution as SolutionRecursive
from problems.p70_climbing_stairs.solution_iterative import Solution as SolutionIterative

TEST_CASES = [
    #pytest.param(2, 2, id="Example 1"),
    #pytest.param(3, 3, id="Example 2"),
    pytest.param(1, 1, id="1 stair"),
    pytest.param(2, 2, id="2 stairs"),
    pytest.param(3, 3, id="3 stairs"),
    pytest.param(4, 5, id="4 stairs"),
    pytest.param(5, 8, id="5 stairs"),
]

@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test_recursive_memo(incoming: int, expected_outcome: int):
    assert SolutionRecursiveMem().climbStairs(incoming) == expected_outcome

@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test_recursive(incoming: int, expected_outcome: int):
    assert SolutionRecursive().climbStairs(incoming) == expected_outcome

@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test_iterative(incoming: int, expected_outcome: int):
    assert SolutionIterative().climbStairs(incoming) == expected_outcome