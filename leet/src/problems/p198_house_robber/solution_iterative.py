from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0] * len(nums)

        for i in range(len(nums)):
            prev = res[i - 2] if i - 2 >= 0 else 0
            prev_2 = res[i - 3] if i - 3 >= 0 else 0

            res[i] = nums[i] + max(prev, prev_2)
            print(i, res)

        return max(res[-1], res[-2])



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