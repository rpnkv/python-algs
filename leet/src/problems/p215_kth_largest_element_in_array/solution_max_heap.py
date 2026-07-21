class Solution:
    # non-optimal
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        nlargest = heapq.nlargest(k, nums)

        res = heapq.heappop_max(nlargest)
        while nlargest:
            res = heapq.heappop_max(nlargest)

        return res

