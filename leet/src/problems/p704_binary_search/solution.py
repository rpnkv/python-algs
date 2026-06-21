class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid_index = l + ((r - l) // 2)
            mid_num = nums[mid_index]

            if mid_num == target:
                return mid_index
            elif mid_num < target:
                l = mid_index + 1
            else:
                r = mid_index - 1

        return -1
