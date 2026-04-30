from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        l_sum = 0

        for i, el in enumerate(nums):
            if total - l_sum - el == l_sum:
                return i

            l_sum += el
        return -1
