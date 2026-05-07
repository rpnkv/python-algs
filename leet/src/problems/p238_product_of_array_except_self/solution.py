from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)

        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]

        post = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]

        res = []

        for i in range(len(nums)):
            res.append(pref[i] * post[i])

        return res
