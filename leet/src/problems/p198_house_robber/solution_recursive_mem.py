from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i: int) -> int:
            if i < 0:
                return 0

            if i < 2:
                #return max(nums[:2])
                return nums[i]

            if i not in dp:
                dp[i] = nums[i] + max(
                    dfs(i - 2),
                    dfs(i - 3)
                )

            return dp[i]

        res_1 = dfs(len(nums) - 1)
        res_2 = dfs(len(nums) - 2)
        return max(res_1, res_2)