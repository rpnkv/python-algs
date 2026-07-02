class Solution:
    # rev2
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = {}
        pairs = 0

        for n in nums:
            target = k - n
            if target in counts and counts[target] > 0:
                counts[target] -= 1
                pairs += 1
            else:
                if n in counts:
                    counts[n] += 1
                else:
                    counts[n] = 1

        return pairs