import pytest

TEST_CASES = [
    pytest.param([[1, 2], [2, 3], [3, 4], [1, 3]], 1, id="example 1"),
    pytest.param([[1, 2], [1, 2], [1, 2]], 2, id="example 2"),
    pytest.param([[1, 2], [2, 3]], 0, id="example 3"),
    pytest.param([[1, 2], [2, 3], [3, 4]], 0, id="non-overlapping"),
    pytest.param([[1,100],[11,22],[1,11],[2,12]], 2, id="case 5"),
]


@pytest.mark.parametrize(["intervals", "expected_output"], TEST_CASES)
def test_solution(intervals: list[list[int]], expected_output: int):
    from problems.p435_non_overlapping_intervals.solution import Solution
    sol = Solution()
    assert sol.eraseOverlapIntervals(intervals) == expected_output


@pytest.mark.parametrize(["intervals", "expected_output"], TEST_CASES)
def test_my_solution(intervals: list[list[int]], expected_output: int):
    from problems.p435_non_overlapping_intervals.greedy_sort import Solution
    sol = Solution()
    assert sol.eraseOverlapIntervals(intervals) == expected_output
