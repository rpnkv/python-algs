import heapq
from typing import List



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify(pq)

        for val in nums[k:]:
            heapq.heappush(pq, val)

            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0]
