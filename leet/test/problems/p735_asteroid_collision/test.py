import pytest

from problems.p735_asteroid_collision.solution import Solution

TEST_CASES = [
    # my cases
    pytest.param([5, 10, 2], [5, 10, 2], id="Positives only"),
    pytest.param([-5, -10, -2], [-5, -10, -2], id="Negatives only"),
    pytest.param([-5, 5], [], id="Mutual destruction collision"),
    pytest.param([-6, 5], [-6], id="Stack wins collision"),
    pytest.param([-4, 5], [5], id="Incoming wins collision"),


    # leetcode cases
    pytest.param([5, 10, -5], [5, 10], id="Example 1"),
    pytest.param([8, -8], [], id="Example 2"),
    pytest.param([10, 2, -5], [10], id="Example 3"),
    pytest.param([3, 5, -6, 2, -1, 4], [-6, 2, 4], id="Example 4"),
]


@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test(incoming: list[int], expected_outcome: list[int]):
    assert Solution().asteroidCollision(incoming) == expected_outcome
