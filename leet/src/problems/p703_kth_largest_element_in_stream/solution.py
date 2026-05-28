from heapq import heapify, heappop, heappushpop, heappush
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        self.k = k
        heapify(self.h)


    def add(self, val: int) -> int:
        heappush(self.h, val)

        while len(self.h) > self.k:
            heappop(self.h)

        return self.h[0]