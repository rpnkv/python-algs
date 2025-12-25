import pytest

from algs.fundamental.arrays.remove_element import remove_element


@pytest.mark.parametrize(
    ["nums", "val", "expected_count"],
    [
        pytest.param([], 0, 0, id="empty"),

        pytest.param([1], 1, 0, id="single matching"),
        pytest.param([1], 2, 1, id="single non-matching"),

        pytest.param([3, 3], 3, 0, id="two matching"),
        pytest.param([3, 3], 2, 2, id="two non-matching"),

        pytest.param([3, 3, 3, 3], 3, 0, id="several matching"),
        pytest.param([3, 3, 3, 3], 2, 4, id="several non-matching"),
        pytest.param([5, 2, 3, 2, 2, 3, 4], 2, 4, id="several partially matching, start with non-matching"),
        pytest.param([2, 5, 3, 2, 2, 3, 4], 2, 4, id="several partially matching, start with matching"),
    ]
)
def test_remove_element(nums: list[int], val: int, expected_count: int):
    assert remove_element(nums, val) == expected_count
    slc = nums[:expected_count]
    assert len([num for num in slc if num == val]) == 0
