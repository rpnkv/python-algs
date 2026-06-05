from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp: list[None | int] = [None] * len(nums)

        def dfs(n: int) -> int:
            if n >= len(nums):
                return 0
            else:
                if not dp[n]:
                    dp[n] = max(
                        dfs(n + 1), dfs(n+2)
                    )

                return dp[n]
        return dfs(0)
