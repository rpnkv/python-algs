class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res: list[list[int]] = []

        l = 0
        m = l + 1
        r = m + 1

        while l < m < r < len(nums):
            s = nums[l] + nums[m] + nums[r]
            if not s:
                res.append([l, m, r])

            if abs(l + m)

        return res


if __name__ == "__main__":
    cases = [
        ([-1, 0, 1], [[0, 1, 2]], "my 1"),
        #([-2, -1 , 0, 1], [[0, 1, 2]], "my 1"),
        # ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]], "example 1"),
        # ([0, 1, 1], [], "example 2"),
        # ([0, 0, 0], [], "example 3"),
    ]

    sol = Solution()

    print()
    for incoming, expected_outcome, case_id in cases:
        print("\tchecking: '" + case_id + "'")

        actual_outcome = sol.threeSum(incoming)

        assert actual_outcome == expected_outcome, "\tFailed for case: '" + case_id + "'"
        print("\tsucceeded: '" + case_id + "'\n")

    print("------ SUCCESS ------")
