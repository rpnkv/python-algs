import pytest

from problems.p1443_longest_common_subsequence.solution_bruteforce import Solution

TEST_CASES = [
    pytest.param("abcde", "ace", 3, id="Example 1"),
    pytest.param("abc", "abc", 3, id="Example 2"),
    pytest.param("abc", "def", 3, id="Example 3"),
]


@pytest.mark.parametrize(["text1", "text2", "expected_outcome"], TEST_CASES)
def test_bruteforce(text1: str, text2: str, expected_outcome: int):
    assert Solution().longestCommonSubsequence(text1, text2) == expected_outcome
