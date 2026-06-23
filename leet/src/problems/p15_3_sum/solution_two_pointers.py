class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []


        for i_l in range(len(nums) - 2):
            if i_l != 0 and nums[i_l] == nums[i_l-1]:
                continue

            i_m, i_r = i_l + 1, len(nums) - 1
            while i_m < i_r:
                n_l = nums[i_l]
                n_m = nums[i_m]
                n_r = nums[i_r]

                curr_sum = n_l + n_m + n_r
                match curr_sum:
                    case x if x == 0:
                        res.append([n_l, n_m, n_r])
                        i_m += 1
                        while i_m < i_r and nums[i_m] == res[-1][1]:
                            i_m += 1
                        while i_m < i_r and nums[i_r] == res[-1][2]:
                            i_r -= 1

                    case x if x < 0:
                        i_m += 1
                    case x if x > 0:
                        i_r -= 1

        return res


if __name__ == "__main__":

    cases = [
        ([-4, -1, -1, 0, 1, 2], [[-1, -1, 2], [-1, 0, 1]], "example 1"),  # sorted

        ([-1, 0, 1], [[-1, 0, 1]], "my 1"),
        ([-2, -1, 0, 3], [[-2, -1, 3]], "my 2"),

        ([0, 0, 0, 0], [[0, 0, 0]], "case 12"),
        ([-1, 0, 1, 0], [[-1, 0, 1]], "case 17"),


        ([0, 1, 1], [], "example 2"),
        ([0, 0, 0], [[0,0,0]], "example 3"),

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
