from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int: # [1, 0, 1], 2
        if len(nums) == 1:
            return 0

        l = 0
        zeroes = 0 if nums[0] else 1
        max_len = 1

        for r in range(1, len(nums)):
            if nums[r] == 0:
                if zeroes == 0:
                    zeroes = 1
                else:
                    while nums[l] != 0 or l == r:
                        l += 1
                    zeroes = 0 if nums[0] else 1

            max_len = max(max_len, r - l + 1)

        return max_len
