class Solution:
    def tribonacci(self, n: int) -> int:
        triplet = [0,1,1]

        if n < 3:
            return triplet[n]

        for i in range(3, n + 1):
            triplet[0], triplet[1], triplet[2] = triplet[1], triplet[2], sum(triplet)

        return triplet[-1]
