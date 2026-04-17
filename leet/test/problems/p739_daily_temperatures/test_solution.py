import pytest

from problems.p739_daily_temperatures.solution import Solution

TEST_CASES = [
    pytest.param([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0], id="example 1"),
    pytest.param([75, 71, 69, 72], [0, 2, 1, 0], id="example 1 subarray"),
    pytest.param([30, 60, 90], [1, 1, 0], id="example 3")
    #pytest.param([73, 74, 75, 71, 69, 72, 76, 73], [74, 75, 76, 72, 76, -1, -1], id="example 1"),
]


@pytest.mark.parametrize(["input_list", "expected_output"], TEST_CASES)
def test(input_list, expected_output):
    assert Solution().dailyTemperatures(input_list) == expected_output
