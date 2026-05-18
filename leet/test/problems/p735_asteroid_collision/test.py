import pytest

from problems.p735_asteroid_collision.solution import Solution

TEST_CASES = [
    # my cases
    pytest.param([5, 10, 2], [5, 10, 2], id="Positives only"),
    pytest.param([-5, -10, -2], [-5, -10, -2], id="Negatives only"),
    pytest.param([5, -5], [], id="Mutual destruction collision"),
    pytest.param([-6, 5], [-6, 5], id="Stack wins collision"),
    pytest.param([-4, 5], [-4, 5], id="Incoming wins collision"),
    # double collision cases
    pytest.param([-4, -3, 5], [-4, -3, 5], id="Double collision reversed pos"),
    pytest.param([4, 3, -5], [-5], id="Double collision reversed neg"),
    # leetcode cases
    pytest.param([5, 10, -5], [5, 10], id="Example 1"),
    pytest.param([8, -8], [], id="Example 2"),
    pytest.param([10, 2, -5], [10], id="Example 3"),
    pytest.param([3, 5, -6, 2, -1, 4], [-6, 2, 4], id="Example 4"),
    pytest.param([-2, -2, 1, -2], [-2, -2, -2], id="Case 250"),
]


@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test(incoming: list[int], expected_outcome: list[int]):
    assert Solution().asteroidCollision(incoming) == expected_outcome
