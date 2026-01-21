from typing import List

import pytest

from problems.medium.p79_word_search.solution_naive import Solution

sol = Solution()


@pytest.mark.parametrize(
    argnames=["board", "word", "expected_output"],
    argvalues=[
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "AB", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
        # submitted test cases
        ([["a", "b"]], "ba", True),
        ([["a", "b"], ["c", "d"]], "acdb", True),
        ([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS", True),
    ]
)
def test_solution(board: List[List[str]], word: str, expected_output: bool):
    assert sol.exist(board, word) == expected_output
