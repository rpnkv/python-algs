class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        width = zeroes = max_width = 0

        for right, num in enumerate(nums):
            width += 1

            zeroes += (0 if num else 1)

            while zeroes > k:
                if not nums[right - width + 1]:
                    zeroes -= 1
                width -= 1


            max_width = max(max_width, width)

        return max_width