class Solution:

    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        triplet = [1, 2, 3]

        for i in range(4, n + 1):
            triplet[0], triplet[1], triplet[2] = triplet[1], triplet[2], sum(triplet[1:])

        return triplet[2]
