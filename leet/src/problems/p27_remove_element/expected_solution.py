class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()

        l = 0

        for r, n in enumerate(nums):
            if n != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        return l