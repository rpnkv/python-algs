class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return [0, 1, 1][n]
        else:
            return sum(
                [self.tribonacci(n - 1), self.tribonacci(n - 2), self.tribonacci(n - 3)]
            )
