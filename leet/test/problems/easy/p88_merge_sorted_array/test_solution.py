import pytest

from problems.easy.p88_merge_sorted_array.solution_advanced import Solution as SolAdvanced
from problems.easy.p88_merge_sorted_array.solution_expected import Solution as SolExpected

TEST_DATA = [
    pytest.param([], 0, [], [], id="both are empty"),
    pytest.param([2, 5, 6], 3, [], [2, 5, 6], id="right is empty"),
    pytest.param([0, 0, 0], 0, [2, 5, 6], [2, 5, 6], id="left is empty"),
    pytest.param([1], 1, [], [1], id="one in the left"),
    pytest.param([0], 0, [1], [1], id="one in the right"),
    pytest.param([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], [1, 2, 2, 3, 5, 6], id="regular case"),
    pytest.param([5, 6, 7, 0, 0, 0], 3, [1, 2, 3], [1, 2, 3, 5, 6, 7], id="moving all l1 elems to right"),
]

sol = SolExpected()
sol_advanced = SolAdvanced()


@pytest.mark.parametrize(["arr1", "arr1_len", "arr2", "expected"], TEST_DATA)
def test_expected(arr1, arr1_len, arr2, expected):
    sol.merge(arr1, arr1_len, arr2, len(arr2))

    assert arr1 == expected


@pytest.mark.parametrize(["arr1", "arr1_len", "arr2", "expected"], TEST_DATA)
def test_advanced(arr1, arr1_len, arr2, expected):
    sol_advanced.merge(arr1, arr1_len, arr2, len(arr2))

    assert arr1 == expected
