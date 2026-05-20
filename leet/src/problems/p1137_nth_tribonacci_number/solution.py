class Solution:
    def tribonacci(self, n: int) -> int:
        triplet = [0,1,1]

        if n < 3:
            return triplet[n]

        s = 0

        for i in range(3, n + 1):
            s = sum(triplet)
            triplet.pop(0)
            triplet.append(s)

        return triplet[-1]

