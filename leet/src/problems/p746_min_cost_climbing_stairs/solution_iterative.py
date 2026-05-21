from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:3] + ([0] * (len(cost) - 3))


        for i in range(2, len(cost)):
            if dp[i - 1] < dp[i - 2]:
                dp[i] = cost[i] + dp[i-1]
            else:
                dp[i] = cost[i] + dp[i - 2]

        return min(dp[-1], dp[-2])
