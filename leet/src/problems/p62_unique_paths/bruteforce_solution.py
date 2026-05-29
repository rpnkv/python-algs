class Solution:
    def uniquePaths(self, m: int, n: int, _m: int = 0, _n: int = 0) -> int:
        if _m == (m - 1)  and _n == (n - 1):
            return 1

        if _m > m or _n > n:
            return 0

        return self.uniquePaths(m, n, _m + 1, _n) + self.uniquePaths(m, n, _m, _n + 1)

