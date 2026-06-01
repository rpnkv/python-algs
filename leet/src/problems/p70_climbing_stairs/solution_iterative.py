class Solution:
    def climbStairs(self, n: int, c: int = 0) -> int:
        steps = [0] * n

        for i in range(n):
            if i in [0, 1]:
                steps[i] =i + 1
            else:
                steps[i] = sum(steps[i - 2:i])

        return steps[-1]
