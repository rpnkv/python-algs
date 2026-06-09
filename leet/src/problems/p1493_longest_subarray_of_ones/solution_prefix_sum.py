class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        backward = [0] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            if not nums[i + 1]:  # prev num breaks the sequence anyway
                backward[i] = 0
            else:  # extend seq
                backward[i] = backward[i + 1] + 1

        forward = [0] * len(nums)

        for i in range(1, len(nums)):
            if not nums[i - 1]:
                forward[i] = 0
            else:
                forward[i] = forward[i - 1] + 1

        result: list[None | int] = [None] * len(nums)

        for i in range(len(nums)):
            result[i] = backward[i] + forward[i]

        return max(result)
