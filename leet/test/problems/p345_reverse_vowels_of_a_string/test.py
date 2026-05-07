import pytest

from problems.p345_reverse_vowels_of_a_string.solution import Solution

TEST_CASES = [
    pytest.param("bcb", "bcb", id="No vowels"),
    pytest.param("bceb", "bceb", id="1 vowel"),
    pytest.param("bceab", "bcaeb", id="2 vowels"),
    pytest.param("bueab", "baeub", id="3 vowels"),
    pytest.param("beueab", "baeueb", id="4 vowels"),
]

@pytest.mark.parametrize(["incoming", "expected_outcome"], TEST_CASES)
def test(incoming: str, expected_outcome: str):
    assert Solution().reverseVowels(incoming) == expected_outcome