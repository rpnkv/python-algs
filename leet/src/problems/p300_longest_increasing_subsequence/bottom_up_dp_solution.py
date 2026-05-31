class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp: list[None | int] = [None] * len(nums)
        dp[0] = 1

        def dfs(nums: list[int], prev_index: int, curr_index) -> int:
            if curr_index >= len(nums):
                return 0

            if nums[prev_index] < nums[curr_index]:
                curr = 1
            else:
                curr = 0

            curr_max = 0

            if curr_index == len(nums) - 1:
                return curr
            else:
                return max(nums[curr_index:]) + curr

        return dfs(nums, 0, 1)
