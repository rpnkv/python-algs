from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:  # [1, 0, 1], 2
        l = 0
        zeroes = 0
        max_width = 0

        for r, num in enumerate(nums):
            if num == 0:
                zeroes += 1

            while zeroes > 1:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1

            curr_width = r - l

            max_width = max(max_width, curr_width)


        return max_width


if __name__ == "__main__":
    cases = [
        # ([1], 0, "my case 1"),
        # ([0], 0, "my case 2"),
        # ([0, 1], 1, "my case 2"),
        # ([1, 1], 1, "my case 4"),
        # ([1, 0], 1, "my case 5"),


        #([0, 1, 0, 1, 0], 3, "my case 5"),

        # ([1, 1, 1], 2, "my case 1"),
        # ([1, 1, 0], 2, "my case 2"),
        # ([1, 1, 0], 2, "my case 3"),
        # ([0, 1, 1], 2, "my case 4"),
        # ([1, 0, 1], 2, "my case 5"),


        ([1,1,0,1], 3, "example 1"),
        ([0,1,1,1,0,1,1,0,1], 5, "example 2"),
        ([1,1,1], 2, "example 3"),
    ]

    sol = Solution()

    for incoming, exp_out, case_id in cases:
        act_out = sol.longestSubarray(incoming)

        assert act_out == exp_out, f"failed {case_id}, res: {act_out}"
