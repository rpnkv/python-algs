# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         import heapq
#
#         h = []
#
#         for n in nums:
#             heapq.heappush(h, n)
#             if len(h) > k:
#                 heapq.heappop(h)
#
#
#         return heapq.heappop(h)
#
#
#

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        h = []

        for n in nums:
            heapq.heappush(h, n)

            if len(h) > k:
                heapq.heappop(h)

        return heapq.heappop(h)