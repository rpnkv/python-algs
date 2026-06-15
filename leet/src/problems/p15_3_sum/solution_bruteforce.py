class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = set()
        nums.sort()

        for l in range(len(nums) - 2):
            for m in range(l + 1, len(nums) - 1):
                for r in range(m + 1, len(nums)):
                    if nums[l] + nums[m] + nums[r] == 0:
                        results.add((nums[l], nums[m], nums[r]))

        return [list(t) for t in results]


if __name__ == "__main__":
    cases = [
        ([-1, 0, 1], [[-1, 0, 1]], "my 1"),
        ([-2, -1, 0, 3], [[-2, -1, 3]], "my 2"),
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]], "example 1"),
        ([0, 1, 1], [], "example 2"),
        ([0, 0, 0], [], "example 3"),
    ]

    sol = Solution()

    print()
    for incoming, expected_outcome, case_id in cases:
        print("\tchecking: '" + case_id + "'")

        actual_outcome = sol.threeSum(incoming)

        for exp_list in expected_outcome:
            assert exp_list in actual_outcome, f"Expected list {exp_list} not found in {actual_outcome}"

        print("\tsucceeded: '" + case_id + "'\n")

    print("------ SUCCESS ------")
