from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(n: int, dp) -> int:
            if n >= len(nums):
                return 0
            else:
                if not dp[n]:
                    dp[n] = nums[n] + max(
                        dfs(n + 2, dp), dfs(n+3, dp)
                    )

                return dp[n]

        dp0: list[None | int] = [None] * len(nums)
        dp1: list[None | int] = [None] * len(nums)

        dfs0 = dfs(0, dp0)
        dfs1 = dfs(1, dp1)

        return max(dfs0, dfs1)



if __name__ == '__main__':
    cases = [
        ([2, 1, 1, 2], 4, "Example X"),
        ([1, 1, 3, 3], 4, "Example 1"),
        ([2, 9, 8, 3, 6], 16, "Example 2"),
    ]

    s = Solution()

    for incoming, expected_outcome, case_id in cases:
        actual_outcome = s.rob(incoming)

        assert actual_outcome == expected_outcome, "case '" + case_id + "' failed: '" + str(actual_outcome) + "'"
        print()

    print("--------- SUCCESS ---------")