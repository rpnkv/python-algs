from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        max_width = 0

        for r, r_el in enumerate(nums):
            if r_el == 0:
                l = r + 1
            else:
                max_width = max(max_width, r - l + 1)


        return max_width


def test(nums: list[int], expected_answer: int):
    assert Solution().findMaxConsecutiveOnes(nums) == expected_answer