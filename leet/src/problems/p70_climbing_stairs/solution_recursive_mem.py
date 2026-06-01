class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def dfs(n) -> int:
            if n < 3:
                return n

            if not n in dp:
                dp[n] = dfs(n - 1) + dfs(n - 2)
            return dp[n]

        return dfs(n)
