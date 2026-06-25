from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = [[1] for _ in range(len(nums))]

        for i, n in enumerate(nums):
            max_len = max(lengths[i])
            for j in range(i + 1, len(nums)):
                o = nums[j]

                if o > n:
                    lengths[j].append(max_len + 1)

        return max([max(len) for len in lengths])

