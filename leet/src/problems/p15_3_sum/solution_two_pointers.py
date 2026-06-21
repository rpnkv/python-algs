class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = list(set(nums))

        results = []
        nums.sort()

        def result() -> list[int]:
            return [nums[l], nums[m], nums[r]]

        for l in range(len(nums) - 2):
            m, r = l + 1, len(nums) - 1

            while m < r:
                s = sum(result())
                if s == 0:
                    results.append(result())
                    m += 1
                    continue

                if s > 0:
                    r -= 1
                else:
                    m += 1

        return results


if __name__ == "__main__":
    cases = [
        # ([-1, 0, 1], [[-1, 0, 1]], "my 1"),
        # ([-2, -1, 0, 3], [[-2, -1, 3]], "my 2"),
        ([-4, -1, -1, 0, 1, 2], [[-1, -1, 2], [-1, 0, 1]], "example 1"),  # sorted
        # ([0, 1, 1], [], "example 2"),
        # ([0, 0, 0], [], "example 3"),
        # ([0, 0, 0, 0], [[0, 0, 0]], "case 12"),
    ]

    sol = Solution()

    print()
    for incoming, expected_outcome, case_id in cases:
        print("\tchecking: '" + case_id + "'")

        actual_outcome = sol.threeSum(incoming)

        if len(actual_outcome) != len(expected_outcome):
            raise Exception(f"Actual {actual_outcome} don't match expected: {expected_outcome} in {case_id}")

        print("\tsucceeded: '" + case_id + "'\n")

    print("------ SUCCESS ------")
