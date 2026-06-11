class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        result = [1, 2]

        for _ in range(n - len(result)):
            result.append(result[-1] + result[-2])

        return result[-1]
