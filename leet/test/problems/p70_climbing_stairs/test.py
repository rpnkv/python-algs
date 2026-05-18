import pytest

from problems.p70_climbing_stairs.solution import Solution

TEST_CASES = [
    pytest.param(2, 2, id="Example 1"),
    pytest.param(3, 3, id="Example 2"),
    pytest.param(5, 8, id="nc explanation example"),
]

@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test(incoming: int, expected_outcome: int):
    assert Solution().climbStairs(incoming) == expected_outcome