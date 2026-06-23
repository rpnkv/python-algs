class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []


        for l in range(len(nums) - 2):
            m, r = l + 1, len(nums) - 1
            while m < r:
                curr_sum = nums[l] + nums[m] + nums[r]
                match curr_sum:
                    case x if x == 0:
                        if (
                            not res
                                or
                            not (res[-1][0] == nums[l] and res[-1][1] == nums[m])
                        ):
                            res.append([nums[l], nums[m], nums[r]])

                        m += 1
                    case x if x < 0:
                        m += 1
                    case x if x > 0:
                        r -= 1

        return res


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
