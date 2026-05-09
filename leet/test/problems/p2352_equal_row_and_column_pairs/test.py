from typing import List

import pytest

from problems.p2352_equal_row_and_column_pairs.solution import Solution

TEST_CASES = [
    pytest.param([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1, id="Example 1"),
    pytest.param([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3, id="Example 2"),
]


@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test(incoming: List[List[int]], expected_outcome: int):
    assert Solution().equalPairs(incoming) == expected_outcome
