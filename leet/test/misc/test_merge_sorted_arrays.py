"""
We're going to test if 'merge of two sorted arrays' implementation is correct.
Presumable corner cases:
1. Left is empty
2. Right is empty
3. Both are empty
4. Both are completely equal
    not implemented 4. Both are distinct and equal size
"""
import pytest

from misc.merge_sorted_arrays import merge


@pytest.mark.parametrize(
    argnames=["left", "right", "expected_output"],
    argvalues=[
        ([], [*range(5)], [*range(5)]),
        ([*range(6)], [], [*range(6)]),
        ([], [], []),
        ([*range(3)], [*range(3)], [0, 0, 1, 1, 2, 2])
    ],
    ids=[
        "left is empty",
        "right is empty",
        "both are empty",
        "both are completely equal"
    ],
)
def test(left, right, expected_output):
    assert merge(left, right) == expected_output
