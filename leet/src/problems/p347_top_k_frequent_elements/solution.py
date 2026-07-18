class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter

        counts = Counter(nums)

        return [key for key, value in heapq.nlargest(k, counts.items(), key=lambda x: x[1])]

if __name__ == "__main__":
    cases = [
        ([1,2,2,3,3,3], 2, [2,3], "example 1")
    ]

    for inc, k, expected, case_id in cases:
        actual = Solution().topKFrequent(inc,k)

        if actual != expected:
            print(f"case {case_id} failed; a/e:{actual}/{expected}")
        else:
            print(f"case {case_id} succeeded")