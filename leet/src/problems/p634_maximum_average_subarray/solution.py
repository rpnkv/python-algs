from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        the_sum = sum(nums[:k])
        the_avg = the_sum / k

        for r in range(k, len(nums)):
            curr_sum = the_sum + nums[r] - nums[r - k]
            the_avg = max(curr_sum / k, the_avg)
            the_sum = curr_sum

        return the_avg
