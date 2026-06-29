class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        pairs = 0

        for n in nums:
            if not n in d:
                d[n] = 1
            else:
                d[n] = d[n] + 1

        for n in nums:
            if n in d:
                if k / n == 2.0:
                    if d[n] >= 2:
                        pairs += 1
                        d[n] = d[n] - 2
                else:
                    if k - n in d:
                        d[n] = d[n] - 1
                        d[k - n] = d[k - n] - 1

                        pairs += 1

                        if d[n] <= 0:
                            del d[n]

                        if d[k - n] <= 0:
                            del d[k - n]

        return pairs

