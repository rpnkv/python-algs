class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        def result() -> list[int]:
            return [nums[l], nums[m], nums[r]]

        for l in range(len(nums) - 2):
            m, r = l + 1, len(nums) - 1
            while m < r:
                n_l = nums[l]
                n_m = nums[m]
                n_r = nums[r]

                curr_sum = n_l + n_m + n_r
                if curr_sum == 0:
                    duplicate = False

                    for prev_l, prev_m, prev_r in reversed(results):
                        if prev_l != n_l:
                            break

                        if prev_m == n_m:
                            duplicate = True
                            break

                    if not duplicate:
                        results.append(result())

                    m += 1

                if sum(result()) > 0:
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
        ([-1, 0, 1, 0], [[-1, 0, 1]], "case 17"),
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
