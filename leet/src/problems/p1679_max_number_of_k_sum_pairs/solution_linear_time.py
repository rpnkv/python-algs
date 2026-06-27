class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # fails for some cases
        s = {n:False for n in nums}
        count = 0

        for n in nums:
            target = k - n
            if target in s and (s[target] == False) and (s[n] == False):
                count += 1
                s[n] = True
                s[k-1] = True

        return
