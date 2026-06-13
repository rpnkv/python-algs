from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0

        for i, n in enumerate(nums):
            if n != 0:
                n_p = i
                break
        else:
            # no zeroes found
            return

        for r in range(n_p, len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1



if __name__ == "__main__":
    cases = [
        ([0, 0, 1, 2], [1, 2, 0, 0], "my example 1"),
        ([1, 0, 0, 2], [1, 2, 0, 0], "my example 2"),
        ([1, 2, 0, 0], [1, 2, 0, 0], "my example 3"),
        ([1, 0, 0, 3, 12], [1, 3, 12, 0, 0], "my example 2"),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0], "example 1"),
        ([0], [0], "example 2"),
    ]

    sol = Solution()

    for incoming, expected_outcome, case_id in cases:
        sol.moveZeroes(incoming)
        assert incoming == expected_outcome, f"failed '{case_id}' + {incoming}"

    print("-- SUCCESS")