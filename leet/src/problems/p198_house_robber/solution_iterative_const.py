from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b,c,d = 0,0,0,0

        for n in nums:
            a, b, c, d = b, c, d, n + max(b, c)

        return max(c,d)



if __name__ == '__main__':
    cases = [
        # ([2, 1, 1, 2], 4, "Example X"),
        # ([1, 1, 3, 3], 4, "Example 1"),
        ([2, 9, 8, 3, 6], 16, "Example 2"),
    ]

    s = Solution()

    for incoming, expected_outcome, case_id in cases:
        actual_outcome = s.rob(incoming)

        assert actual_outcome == expected_outcome, "case '" + case_id + "' failed: '" + str(actual_outcome) + "'"
        print()

    print("--------- SUCCESS ---------")