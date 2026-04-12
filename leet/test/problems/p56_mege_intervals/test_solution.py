import pytest

from problems.p56_merge_intervals.solution import Solution

TEST_CASES = [
    pytest.param([[1, 2], [3, 4]], [[1, 2], [3, 4]], id="non-overlapping 2", ),
    pytest.param([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]], id="non-overlapping 3", ),
    pytest.param([[1, 2], [3, 4]], [[1, 2], [3, 4]], id="non-overlapping", ),
]


@pytest.mark.parametrize(["input_intervals", "expected_output"], TEST_CASES)
def test(input_intervals: list[list[int]], expected_output: list[list[int]]):
    sol = Solution()
    assert sol.merge(input_intervals) == expected_output
