from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ex1: [1, 1, 2, 8]
        l_to_r = [1] * len(nums)
        for i in range(1, len(nums)):
            l_to_r[i] = l_to_r[i - 1] * nums[i - 1]


        # ex2: [48, 24, 6, 1]
        r_to_l = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            r_to_l[i] = r_to_l[i + 1] * nums[i + 1]


        res = []

        for i in range(len(nums)):
            res.append(l_to_r[i] * r_to_l[i])

        return res
