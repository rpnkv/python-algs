from problems.easy.p88_merge_sorted_array.solution_expected import Solution as SolExpected
from problems.easy.p88_merge_sorted_array.solution_advanced import Solution as SolAdvanced

sol = SolExpected()
sol_advanced = SolAdvanced()

def test_expected():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    expected_output = [1, 2, 2, 3, 5, 6]

    sol.merge(nums1, m, nums2, n)

    assert nums1 == expected_output


def test_advanced():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    expected_output = [1, 2, 2, 3, 5, 6]

    sol_advanced.merge(nums1, m, nums2, n)

    assert nums1 == expected_output
