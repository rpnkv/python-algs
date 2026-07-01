from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = max_s = sum(nums[:k])

        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            max_s = max(max_s, s)


        return max_s / k
