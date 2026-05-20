class Solution:

    def __init__(self):
        self.results: dict[int, int] = {}

    def climbStairs(self, n: int, s: int = 0) -> int:
        if s in self.results:
            return self.results[s]

        if n == s:
            self.results[s] = 1
            return 1

        if n < s:
            self.results[s] = 0
            return 0
        else:
            curr_res = self.climbStairs(n, s + 1) + self.climbStairs(n, s + 2)
            self.results[s] = curr_res
            return curr_res
