import pytest

from problems.p127_word_ladder.solution import Solution


@pytest.mark.parametrize(
    argnames=["current_word", "checking_word", "expected_result"],
    argvalues=[
        # 1 letter
        ("w", "w", False),
        ("w", "x", True),
        ("w", "a", True),
        # 2 letters
        ("ww", "ww", False),
        ("ww", "wa", True),
        ("ww", "aa", False),
        ("ww", "aw", True),
        # 3 letters
        ("www", "www", False),
        ("www", "wwa", True),
        ("www", "waa", False),
        ("www", "aaa", False),
        ("www", "aww", True),
        ("www", "aaw", False),
        ("www", "waw", True),
    ]
)
def test_check_if_one_letter_differs(current_word, checking_word, expected_result: bool):
    assert Solution._check_if_one_letter_differs(current_word, checking_word) == expected_result

@pytest.mark.parametrize(
    argnames=["current_word", "all_routes", "possible_routes"],
    argvalues=[
        ("cat", [], []),
        ("cat", ["car"], ["car"]),
        ("cat", ["car", "cax"], ["car", "cax"]),
        ("cat", ["car", "cax", "cor"], ["car", "cax"]),
    ]
)
def test_define_possible_routes(current_word: str, all_routes: list[str], possible_routes:list[str]):
    assert Solution._define_possible_routes(current_word, all_routes) == possible_routes


sol = Solution()


@pytest.mark.parametrize(
    argnames=["begin_word", "end_word", "word_list", "expected_output"],
    argvalues=[
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ],
    ids=["example1", "example2"]
)
def test_solution_completely(begin_word: str, end_word: str, word_list: list[str], expected_output: int):
    assert sol.ladderLength(begin_word, end_word, word_list) == expected_output
