class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(n) -> int:
            if n < 3:
                return n
            else:
                return dfs(n - 1) + dfs(n - 2)

        return dfs(n)
