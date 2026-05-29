class Solution:
    def __init__(self):
        self.dp = None

    def uniquePaths(self, m: int, n: int, _m: int = 0, _n: int = 0) -> int:
        if _m == (m - 1) and _n == (n - 1):
            return 1

        if _m >= m or _n >= n:
            return 0

        if not self.dp:
            self.dp = []
            for i in range(m):
                self.dp.append([None] * n)

        if not self.dp[_m][_n]:
            paths = self.uniquePaths(m, n, _m + 1, _n) + self.uniquePaths(m, n, _m, _n + 1)
            self.dp[_m][_n] = paths

        return self.dp[_m][_n]
