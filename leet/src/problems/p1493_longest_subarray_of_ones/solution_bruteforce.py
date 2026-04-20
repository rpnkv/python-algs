from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int: # [1, 0, 1], 2
        max_len = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                has_zeroes = False
                for k, el in enumerate(nums[i:j]):
                    raise NotImplementedError

