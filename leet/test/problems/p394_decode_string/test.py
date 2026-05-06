import pytest

from problems.p394_decode_string.solution import Solution

TEST_CASES = [
    pytest.param("3[a]2[bc]", "aaabcbc", id="Example 1"),
    pytest.param("3[a2[c]]", "accaccacc", id="Example 2"),
    pytest.param("2[abc]3[cd]ef", "abcabccdcdcdef", id="Example 3"),
]


@pytest.mark.parametrize(["incoming", "expected"], TEST_CASES)
def test(incoming: str, expected: str):
    assert Solution().decodeString(incoming) == expected
