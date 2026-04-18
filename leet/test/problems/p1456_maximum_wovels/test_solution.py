import pytest

from problems.p1456_maximum_wovels.solution import Solution

TEST_CASES = [
    pytest.param("abciiidef", 3, 3),
    pytest.param("leetcode", 3, 2)
]


@pytest.mark.parametrize(["s", "k", "expected_answer"], TEST_CASES)
def test(s: str, k: int, expected_answer: int) -> None:
    assert Solution().maxVowels(s, k) == expected_answer
