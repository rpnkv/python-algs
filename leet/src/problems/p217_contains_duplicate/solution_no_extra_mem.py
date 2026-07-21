class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i, n in enumerate(nums[1:]):
            if nums[i] == n:
                return True

        return False


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 1], True, "ex 1"),
        ([1, 2, 3, 4], False, "ex 2"),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True, "ex 3"),
    ]

    for inp, o_exp, case_id in cases:
        o_act = Solution().containsDuplicate(inp)

        assert o_act == o_exp, f"failed for case {case_id}"
