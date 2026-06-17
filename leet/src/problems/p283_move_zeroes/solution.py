class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0

        for r, num in enumerate(nums):
            if num != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1





if __name__ == "__main__":
    cases = [
        ([0], [0], "single zero"),
        ([1], [1], "single num"),
        ([0, 1], [1, 0], "2 nums leading zero"),
        ([1, 0], [1, 0], "2 nums leading num"),
        ([1, 1, 0], [1, 1, 0], "2 nums, 1 zero, leading num"),
        ([1, 0, 1], [1, 0, 1], "2 nums, 1 zero, middle zero"),
        ([0, 1, 1], [0, 1, 1], "2 nums, 1 zero, middle zero"),
        ([0, 1, 1, 0], [1, 2, 0, 0], "2 nums, 2 zeroes, nums middle"),
        ([1, 2, 0, 0], [1, 2, 0, 0], "2 nums, 2 zeroes, nums left"),
        ([0, 0, 1, 2], [1, 2, 0, 0], "2 nums, 2 zeroes, nums right"),
        ([0, 1, 2, 0], [1, 2, 0, 0], "2 nums, 2 zeroes, zeroes middle"),
    ]

    sol = Solution()

    for incoming, exp_outcome, case_id in cases:
        sol.moveZeroes(incoming)

        assert incoming == exp_outcome, f"failed for {case_id}: {incoming}"

    print("-- SUCCESS")
