import heapq
from typing import List



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        for num in nums:
            heapq.heappush_max(h, num)
            if len(h) > k:
                h.pop()

        return h.pop()



