import pytest

from algs.fundamental.arrays.merge_two_sorted_lists import merge

TEST_VALUES=[
    pytest.param([*range(5)], [*range(5, 10)], [*range(10)], id="non-intersected"),
    pytest.param([*range(9)][::2], [*range(1,10)][::2], [*range(10)], id="fully intersected")
]

@pytest.mark.parametrize(["list1", "list2", "expected_list"], TEST_VALUES)
def test_merge(list1, list2, expected_list):
    assert merge(list1, list2) == expected_list
