import pytest

from problems.p208_implement_trie.solution import Trie

TEST_CASES = [
    pytest.param(
        [
            (Trie.insert, "apple", None),
            (Trie.search, "apple", True),
            (Trie.search, "app", False),
            (Trie.startsWith, "app", True),
            (Trie.insert, "app", None),
            (Trie.search, "app", True),
        ], id="Example 1"
    ),
    pytest.param(
        [
            (Trie.insert, "aab", None),
            (Trie.insert, "abb", None),
            (Trie.insert, "bac", None),
        ], id="My insertion test"
    ),
    pytest.param(
        [
            (Trie.insert, "aab", None),
            (Trie.search, "aab", True),
            (Trie.search, "aac", False),
            (Trie.search, "aa", False),
        ], id="My search"
    )
]

@pytest.mark.parametrize(["actions"], TEST_CASES)
def test(actions: list):
    trie = Trie()

    for fn, arg, expected in actions:
        assert fn(trie, arg) == expected