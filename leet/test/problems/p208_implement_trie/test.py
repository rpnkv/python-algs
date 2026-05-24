import pytest

from problems.p208_implement_trie.solution import Trie

TEST_CASES = [
    pytest.param(
        [
            (Trie.insert, "apple", None),
            (Trie.search, "apple", True),
        ], id="Example 1"
    )
]

@pytest.mark.parametrize(["actions"], TEST_CASES)
def test(actions: list):
    trie = Trie()

    for fn, arg, expected in actions:
        assert fn(trie, arg) == expected