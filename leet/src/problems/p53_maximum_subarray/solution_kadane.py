class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = float('-inf')
        current_sum = None

        for x in nums:
            if not current_sum:
                current_sum = x
            else:
                current_sum = max(x, current_sum + x)

            best_sum = max(best_sum, current_sum)

        return best_sum
