import pytest

from problems.p127_word_ladder.solution import Solution

sol = Solution()


@pytest.mark.parametrize(
    argnames=["begin_word", "end_word", "word_list", "expected_output"],
    argvalues=[
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ],
    ids=["example1", "example2"]
)
def test_solution(begin_word: str, end_word: str, word_list: list[str], expected_output: int):
    assert sol.ladderLength(begin_word, end_word, word_list) == expected_output
