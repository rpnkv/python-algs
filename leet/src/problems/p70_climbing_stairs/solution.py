class Solution:
    def climbStairs(self, n: int, s: int = 0) -> int:
        if n == s:
            return 1

        if n < s:
            return 0
        else:
            return self.climbStairs(n, s + 1) + self.climbStairs(n, s + 2)
