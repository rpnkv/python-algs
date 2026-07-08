from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        l = 0
        ln = ln_max = 0 if not nums else 1

        for r, num in enumerate(nums):
            if num != nums[l]:
                if num == nums[l] + 1:
                    ln += 1
                else:
                    ln = 1

                l = r

            ln_max = max(ln_max, ln)

        return ln_max

if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4], 4),
        ([1, 2, 4, 5], 2),
        ([1, 2, 2, 3, 4], 4),
        ([1, 2, 2, 3], 3),
        ([1, 2, 2, 0, 1, 2], 3),
        ([1, 2, 3, 4, 100, 200], 4),
    ]

    sol = Solution()

    for incoming, expected_outcome in cases:
        actual_outcome = sol.longestConsecutive(incoming)
        assert actual_outcome == expected_outcome, f"failed for {sorted(incoming)}, {actual_outcome}"
        print(f"success for {incoming}")

    print("-- SUCCESS!")
