class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]

        for i, n  in enumerate(nums):
            curr_sub = None
            for j in range(i, len(nums)):
                if not curr_sub:
                    curr_sub = nums[j]
                else:
                    curr_sub += nums[j]

                max_sub = max(max_sub, curr_sub)

        return max_sub


if __name__ == "__main__":
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "example 1"),
        ([5, 4, -1, 7, 8], 23, "case 4 nc"),
        ([-2,1], 1, "case 6 nc"),
        ([-1, -2], -1, "case 9 nc"),
    ]

    for inc, exp, case in cases:
        act = Solution().maxSubArray(inc)

        if act != exp:
            print(f"failed {case}, exp: {exp}, act: {act}")
        else:
            print(f"{case} succeeded")
