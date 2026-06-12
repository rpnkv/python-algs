from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        results = []
        # ex_X: 0(2)=2; 1(1)=1; 2(1)=3; 3(2)=4

        for i in range(len(nums)):
            prev_1 = prev_2 = 0

            if i - 2 >= 0:
                prev_1 = results[i-2]

            if i - 3 >= 0:
                prev_2 = results[i-3]

            results.append(max(prev_1, prev_2) + nums[i])
        return max(results[-1], results[-2]) if len(results) > 1 else results[0]



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

    print("--------- SUCCESS ---------")