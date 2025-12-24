import pytest

from problems.easy.p88_merge_sorted_array.solution_advanced import Solution as SolAdvanced
from problems.easy.p88_merge_sorted_array.solution_expected import Solution as SolExpected

TEST_DATA = [
    pytest.param([1, 2, 3, 0, 0, 0], [2, 5, 6], [1, 2, 2, 3, 5, 6], id="case1")
]

sol = SolExpected()
sol_advanced = SolAdvanced()


@pytest.mark.parametrize(["arr1", "arr2", "expected"], TEST_DATA)
def test_expected(arr1, arr2, expected):
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    expected_output = [1, 2, 2, 3, 5, 6]

    sol.merge(nums1, m, nums2, n)

    assert nums1 == expected_output


@pytest.mark.parametrize(["arr1", "arr2", "expected"], TEST_DATA)
def test_advanced(arr1, arr2, expected):
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    expected_output = [1, 2, 2, 3, 5, 6]

    sol_advanced.merge(nums1, m, nums2, n)

    assert nums1 == expected_output
