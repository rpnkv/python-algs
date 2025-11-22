import pytest

from problems.medium.p3_longest_substring_no_repeating.solution import Solution


@pytest.mark.parametrize(
    argnames=["input_str", "expected_output"],
    argvalues=[
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("dvdf", 3),
        ("ohvhjdml", 6),
    ],
    ids=[
        "test case 1",
        "test case 2",
        "test case 3",
        "test case 225",
        "test case 590"
    ]
)
def test(input_str: str, expected_output: int):
    sol = Solution()
    assert sol.lengthOfLongestSubstring(input_str) == expected_output
