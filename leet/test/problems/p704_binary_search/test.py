import pytest

from problems.p704_binary_search.solution import Solution

TEST_CASES = [
    pytest.param([-1, 0, 3, 5, 9, 12], 9, 4, id="Example 1"),
    pytest.param([-1, 0, 3, 5, 9, 12], 2, -1, id="Example 2"),
    pytest.param([5], 5, 0, id="Case 8"),
    pytest.param([-1,0,3,5,9,12], 12, 5, id="Case 12"),
]


@pytest.mark.parametrize(["incoming", "target", "expected_outcome"], TEST_CASES)
def test(incoming: list[int], target: int, expected_outcome: int):
    sol = Solution()

    assert sol.search(incoming, target) == expected_outcome
