class Solution:
    def climbStairs(self, n: int) -> int:
        dp: list[int | None] = [None] * n
        for i in range(min(n, 2)):
            dp[i] = i

        def dfs(n) -> int:
            if not dp[n]:
                dp[n] = dfs(n - 1) + dfs(n - 2)
            return dp[n]

        return dfs(n)
