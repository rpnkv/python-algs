class Solution:
    def climbStairs(self, n: int, c: int = 0) -> int:
        if c >= n:
            return 1
        else:
            return self.climbStairs(n, c + 1) + self.climbStairs(n, c + 2)
