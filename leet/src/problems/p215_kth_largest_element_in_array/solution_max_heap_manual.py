class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        h = nums[:k]
        heapq.heapify_max(h)

        for n in nums[k:]:
            heapq.heappush_max(h, n)
            #heapq.heappop_max(h)
            h.pop()

        res = 0
        for _ in range(k):
            res = heapq.heappop_max(h)

        return res