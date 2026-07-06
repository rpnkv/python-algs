import heapq

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1

        h = []
        for n, freq in freqs.items():
            heapq.heappush(h, (freq, n))
            if len(h) > k:
                heapq.heappop(h) 

        return [el[1] for el in h]

if __name__ == "__main__":
    cases = [
        ([1,2,2,3,3,3], 2, [2,3], "example 1")
    ]

    for inc, k, expected, case_id in cases:
        actual = Solution().topKFrequent(inc,k)

        if actual != expected:
            print(f"case {case_id} failed")
        else:
            print(f"case {case_id} succeeded")