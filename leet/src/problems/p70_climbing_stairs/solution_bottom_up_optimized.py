class Solution:
    def climbStairs(self, n: int) -> int:
        prev_sub_1, prev_sub_2 = 2, 1

        for i in range(3, n):

