class Solution:
    # non-optimal
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        h = nums[:k]

        heapq.heapify(h)

        for n in nums[k:]:
            heapq.heappush(h, n)
            heapq.heappop(h)

        for _ in range(k - 1):
            heapq.heappop(h)

        return heapq.heappop(h)