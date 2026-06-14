class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z = n = 0

        #while z < len(nums) and n < len(nums):
        while True:
            while nums[z] != 0:
                z += 1
                if z >= len(nums):
                    return

            while nums[n] == 0:
                n +=1
                if n >= len(nums):
                    return

            nums[n], nums[z] = nums[z], nums[n]





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
