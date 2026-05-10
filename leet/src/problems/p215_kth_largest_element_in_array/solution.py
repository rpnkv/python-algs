import heapq
from typing import List



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        for num in nums:
            heapq.heappush_max(h, num)

        for _ in range(k - 1):
            heapq.heappop_max(h)

        return heapq.heappop_max(h)




