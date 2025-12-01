"""
We're going to test if 'merge of two sorted arrays' implementation is correct.
Presumable corner cases:
1. Left is empty
2. Right is empty
3. Both are empty
4. Both are distinct and equal size
5. Both are completely equal
"""
import pytest

from misc.merge_sorted_arrays import merge


@pytest.mark.parametrize(
    argnames=["left", "right", "expected_output"],
    argvalues=[],
    ids=[],
)
def test(left, right, expected_output):
    assert merge(left, right) == expected_output
