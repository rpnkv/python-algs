import pytest

cases = [
    pytest.param("ababababc", ["abababa", "bababab"], id="manacher example case"),
    # pytest.param("aacabdkacaa", ["aca"], id="case 17"),
    # pytest.param("abbc", ["bb"], id="case 1"),
    # pytest.param("a", ["a"], id="case 3"),
    # pytest.param("abcba", ["abcba"], id="full centered"),
    # pytest.param("abcde", [c for c in "abcde"], id="no palindromes"),
    # pytest.param("abade", ["aba"], id="1-started"),
    # pytest.param("acded", ["ded"], id="3-started"),
    # pytest.param("abbc", ["bb"], id="example 2"),
]


@pytest.mark.parametrize(["inc", "exp"], cases)
def test_expand_around_center(inc: str, exp: list[str]):
    from problems.p5_longest_palindromic_substring.solution_cetner_search import Solution
    sol = Solution()

    act = sol.longestPalindrome(inc)

    for appropriate in exp:
        if appropriate == act:
            return

    raise AssertionError(f"Res {act} doesn't match any of expected: {exp}")


@pytest.mark.parametrize(["inc", "exp"], cases)
def test_expand_manacher(inc: str, exp: list[str]):
    from problems.p5_longest_palindromic_substring.solution_manacher import Solution
    sol = Solution()

    act = sol.longestPalindrome(inc)

    for appropriate in exp:
        if appropriate == act:
            return

    raise AssertionError(f"Res {act} doesn't match any of expected: {exp}")
