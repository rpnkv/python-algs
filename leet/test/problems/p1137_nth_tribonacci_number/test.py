import pytest

from problems.p1137_nth_tribonacci_number.solution import Solution

TEST_CASES = [
    pytest.param(0, 0, id="Pre-defined case 0"),
    pytest.param(1, 1, id="Pre-defined case 1"),
    pytest.param(2, 1, id="Pre-defined case 2"),
    pytest.param(3, 2, id="Pre-defined case 3"),
    pytest.param(4, 4, id="Example 1"),
    pytest.param(25, 1389537, id="Example 2"),
]

@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test(incoming:int, expected_outcome:int):
    assert Solution().tribonacci(incoming) == expected_outcome