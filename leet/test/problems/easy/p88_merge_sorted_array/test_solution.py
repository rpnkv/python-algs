from problems.easy.p88_merge_sorted_adday.solution_expected import Solution

sol = Solution()


def test0():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    expected_output = [1, 2, 2, 3, 5, 6]

    sol.merge(nums1, m, nums2, n)

    assert nums1 == expected_output
