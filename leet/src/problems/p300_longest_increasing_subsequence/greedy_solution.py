from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            pos = bisect_left(tails, x)
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
        return len(tails)