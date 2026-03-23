from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        vacant: int = None

        for i in range(len(nums)):
            if nums[i] == val:
                vacant = i
                break
        else:
            return val

        seeking = vacant + 1

        while seeking < len(nums):
            if nums[seeking] != val:
                nums[vacant] = nums[seeking]
                vacant += 1
            seeking += 1

        return vacant
