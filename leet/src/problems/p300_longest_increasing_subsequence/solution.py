class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(nums: list[int], prev: int) -> int:
            if not nums:
                return 0

            if nums[0] > prev:
                curr = 1
            else:
                curr = 0

            subseqs = []


            for n in range(1, len(nums)):
                subseqs.append(dfs(nums[1:], nums[0]))

            if subseqs:
                return max(subseqs) + curr
            else:
                return curr


        return dfs(nums, -1001)