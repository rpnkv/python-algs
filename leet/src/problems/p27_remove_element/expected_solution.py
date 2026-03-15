from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        vacant = -1

        for i in range(len(nums)):
            vacant = i
            if nums[i] == val:
                break
        else:
            return vacant + 1

        seeking = vacant + 1

        for i in range(seeking, len(nums)):
            if nums[i] != val:
                nums[vacant] = nums[i]
                vacant += 1


        return vacant

