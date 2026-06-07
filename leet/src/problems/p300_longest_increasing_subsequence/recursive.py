from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def check(nums: List[int]) -> int:
            if not nums:
                return 0

            if len(nums) == 1:
                return 1

            subseq_len = check(nums[1:])
            if nums[0] < nums[1]:
                return 1 + subseq_len
            else:
                return subseq_len

        return check(nums)
