class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_width = 0
        width = 0
        zeroes = 0

        for i, n in enumerate(nums):
            width += 1

            if n == 0:
                zeroes += 1

            while zeroes > k and width > 0:
                if nums[i - width + 1] == 0:
                    zeroes -= 1
                width -= 1

            max_width = max(max_width, width)

        return max_width