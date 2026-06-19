from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        curr_len = max_len = 1
        l = 0

        for r in range(1, len(nums)):
            if nums[r] == nums[l]:
                continue
            else:
                if nums[l] + 1 == nums[r]:
                    curr_len += 1
                else:
                    curr_len = 1
                l = r

                max_len = max(max_len, curr_len)

        return max_len


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
