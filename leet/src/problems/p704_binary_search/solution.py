class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            match nums[mid]:
                case m if m == target:
                    return mid
                case m if m < target:
                    r = mid - 1
                case m if m > target:
                    l = mid + 1

        return -1