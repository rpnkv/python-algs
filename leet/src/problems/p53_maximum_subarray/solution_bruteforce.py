class SolutionBruteforce:
    def maxSubArray(self, nums: List[int]) -> int:
        n_len = len(nums)

        s_max = max(nums)

        for i in range(n_len):
            start_sum = nums[i]
            s_max = max(start_sum, s_max)
            for j in range(i, n_len):
                # for j in range(i + 1, n_len + 1):
                # s_max = max(s_max, sum(nums[i:j])) # very
                start_sum += nums[j]
                s_max = max(start_sum, s_max)

        return s_max


if __name__ == "__main__":
    cases = [
        # ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "example 1"),
        # ([5, 4, -1, 7, 8], 23, "case 4 nc"),
        # ([-2,1], 1, "case 6 nc"),
        ([-1, -2], -1, "case 9 nc"),
    ]

    for inc, exp, case in cases:
        act = SolutionBruteforce().maxSubArray(inc)

        if act != exp:
            print(f"failed {case}, exp: {exp}, act: {act}")
        else:
            print(f"{case} succeeded")
