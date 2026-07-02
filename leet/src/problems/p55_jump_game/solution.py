class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0

        for i, n in enumerate(nums):
            if max_index >= i:
                max_index = max(max_index, i + n)
            else:
                return False

        return True


if __name__ == "__main__":
    cases = [
        ([1,2,0,1,0], True, "example 1"),
        ([1,2,1,0,1], False, "example 2"),
    ]

    for inc, exp, case_id in cases:
        actual = Solution().canJump(inc)

        assert actual == exp