from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # [1, 12, -5, -6, 50, 3]; 4
        l = curr_sum = 0
        max_avg = -10001

        for r in range(len(nums)):
            curr_sum += nums[r]

            if (r - l + 1) > k:
                curr_sum -= nums[l]
                l+=1

            if (r - l + 1) == k:
                max_avg = max(max_avg, curr_sum / k)


        return max_avg
