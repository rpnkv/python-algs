class SolutionBruteforce:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)

        for i, n in enumerate(nums):
            curr_sum = n
            for k in range(i+1, len(nums)):
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)

        return max_sum


if __name__ == "__main__":
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "example 1"),
        ([5, 4, -1, 7, 8], 23, "case 4 nc"),
        ([-2,1], 1, "case 6 nc"),
        ([-1, -2], -1, "case 9 nc"),
    ]

    for inc, exp, case in cases:
        act = SolutionBruteforce().maxSubArray(inc)

        if act != exp:
            print(f"failed {case}, exp: {exp}, act: {act}")
        else:
            print(f"{case} succeeded")
