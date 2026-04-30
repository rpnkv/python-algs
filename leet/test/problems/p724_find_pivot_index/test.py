import pytest

from problems.p724_find_pivot_index.solution import Solution

TEST_CASES = [
    pytest.param([1, 7, 3, 6, 5, 6], 3, id="Example 1"),
    pytest.param([1, 2, 3], -1, id="Example 2"),
    pytest.param([2, -1, 1], 0, id="Example 3"),
]


@pytest.mark.parametrize(["input_list", "expected_answer"], TEST_CASES)
def test(input_list: list[int], expected_answer: int):
    assert Solution().pivotIndex(input_list) == expected_answer
