import pytest

from problems.p1143_longest_common_subsequence.solution_bruteforce import Solution

CASES = [
    pytest.param("abc", "abbc", 3, id="my 1"),
]


@pytest.mark.parametrize(["text1", "text2", "exp"], CASES)
def test_bruteforce(text1: str, text2: str, exp: int):
    actual = Solution().longestCommonSubsequence(text1, text2)
    assert actual == exp
