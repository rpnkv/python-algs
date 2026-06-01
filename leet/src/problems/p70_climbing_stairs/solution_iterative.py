class Solution:
    def climbStairs(self, n: int, c: int = 0) -> int:
        steps = [0] * n

        for i in range(n):
            if i < 2:
                steps[i] =i + 1
            else:
                steps[i] = steps[i-1] + steps[i-2]

        return steps[-1]
