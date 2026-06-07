class Solution:
    def rob(self, nums: List[int]) -> int:
        money = [0] * len(nums)

        for i in range(min(2, len(nums))):
            money[i] = nums[i]

        for i in range(2, len(money)):
            money[i] = nums[i] + max(money[max(0,i-3):i-1])

        return max(money)