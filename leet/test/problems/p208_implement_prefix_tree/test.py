import pytest

from problems.p208_implement_prefix_tree.solution import PrefixTree

TEST_CASES = [
    pytest.param(
        [
            (PrefixTree.insert, "apple", None),
            (PrefixTree.search, "apple", True),
            (PrefixTree.search, "app", False),
            (PrefixTree.startsWith, "app", True),
            (PrefixTree.insert, "app", None),
            (PrefixTree.search, "app", True),
        ], id="Example 1"
    ),
    pytest.param(
        [
            (PrefixTree.insert, "aab", None),
            (PrefixTree.insert, "abb", None),
            (PrefixTree.insert, "bac", None),
        ], id="My insertion test"
    ),
    pytest.param(
        [
            (PrefixTree.insert, "aab", None),
            (PrefixTree.search, "aab", True),
            (PrefixTree.search, "aac", False),
            (PrefixTree.search, "aa", False),
            (PrefixTree.search, "aab", True),
        ], id="My search"
    )
]

@pytest.mark.parametrize(["actions"], TEST_CASES)
def test(actions: list):
    pt = PrefixTree()

    for fn, arg, expected in actions:
        assert fn(pt, arg) == expected