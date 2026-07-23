class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import bisect

        i = bisect.bisect_left(nums, target)

        if i == len(nums):
            return -1

        if nums[i] == target:
            return i
        else:
            return -1