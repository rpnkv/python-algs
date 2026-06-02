from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        max_len = 0

        for n in nums:
            length = 1
            while n + 1 in s:
                length += 1
                n = n + 1

            max_len = max(max_len, length)

        return max_len
