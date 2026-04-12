import pytest

from problems.p56_merge_intervals.solution import Solution

TEST_CASES = [
    pytest.param([[1, 2], [3, 4]], [[1, 2], [3, 4]], id="non-overlapping 2", ),
    pytest.param([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]], id="non-overlapping 3", ),
    pytest.param([[1, 2], [2, 3]], [[1, 3]], id="2 neighboor intervals"),
    pytest.param([[1, 4], [2, 3]], [[1, 4]], id="fully overlap intervals"),
    pytest.param([[1, 10], [2, 3], [4,6]], [[1, 10]], id="fully overlap intervals 2"),
    pytest.param([[1, 10], [2, 3], [4,11]], [[1, 11]], id="fully overlap intervals 3"),
]


@pytest.mark.parametrize(["input_intervals", "expected_output"], TEST_CASES)
def test(input_intervals: list[list[int]], expected_output: list[list[int]]):
    sol = Solution()
    assert sol.merge(input_intervals) == expected_output
