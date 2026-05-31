import pytest

from problems.p3_longest_substring_no_repeating.solution import Solution

TEST_CASES = [
    pytest.param("abcabcbb", 3, id="Test case 1"),
    pytest.param("bbbbb", 1, id="Test case 2"),
    pytest.param("pwwkew", 3, id="Test case 3"),
    pytest.param("dvdf", 3, id="Test case 225"),
    pytest.param("ohvhjdml", 3, id="Test case 590"),
]


@pytest.mark.parametrize(["input_str", "expected_output"], TEST_CASES)
def test(input_str: str, expected_output: int):
    sol = Solution()
    assert sol.lengthOfLongestSubstring(input_str) == expected_output
