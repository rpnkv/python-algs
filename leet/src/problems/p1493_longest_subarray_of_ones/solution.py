from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        zeroes = 0
        max_len = 0

        while r < len(nums):
            if l == r and nums[r] == 0:
                l += 1
                r += 1
                continue

            if l == r and nums[r] == 1:
                r += 1
                continue

            if nums[r] == 0:
                if zeroes == 0:
                    zeroes = 1
                    r += 1
                else:
                    while zeroes > 0 and r != l:
                        if nums[l] == 0:
                            zeroes = 0

                        l += 1
                    continue
            else:
                r += 1

            max_len = max(max_len, r - l - zeroes)

        return max_len
