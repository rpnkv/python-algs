class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        raise NotImplementedError


if __name__ == "__main__":
    cases = [
        ([-2, 0, 0, 0, 0, 2, 2], [[-2, 2], [0, 0]], "case 1"),
    ]
    sol = Solution()

    print()
    for incoming, expected_outcome, case_id in cases:
        print("\tchecking: '" + case_id + "'")

        actual_outcome = sol.threeSum(incoming)

        if actual_outcome != expected_outcome:
            raise Exception(f"Actual {actual_outcome} don't match expected: {expected_outcome} in {case_id}")

        print("\tsucceeded: '" + case_id + "'\n")

    print("------ SUCCESS ------")
