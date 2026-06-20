class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if l == r:
                return r if nums[l] == target else -1

            mid_index = l + ((r - l) // 2)

            match nums[mid_index]:
                case num if target < num:
                    r = mid_index - 1
                case num if target > num:
                    l = mid_index + 1
                case num if num == target:
                    return mid_index

        return -1
