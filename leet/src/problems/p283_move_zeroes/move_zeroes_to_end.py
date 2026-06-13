from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) in [0,1]:
            return

        insert_position = -1 # where we will insert next non-zero value
        seek_position = -1 # looking for zeroes

        for i in range(len(nums)):
            insert_position = i
            seek_position = i + 1

            if nums[i] == 0:
                break


        while seek_position < len(nums):
            if nums[seek_position] != 0:
                nums[insert_position], nums[seek_position] = nums[seek_position], nums[insert_position]
                insert_position += 1

            seek_position += 1
