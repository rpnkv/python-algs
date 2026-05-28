from heapq import heapify, heappop, heappushpop
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        self.k = k
        heapify(self.h)

        while len(self.h) > k:
            heappop(self.h)

    def add(self, val: int) -> int:
        heappushpop(self.h, val)
        return self.h[0]
