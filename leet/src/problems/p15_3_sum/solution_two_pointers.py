class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for l in range(len(nums) - 2):
            if l > 0 and nums[l - 1] == nums[l]:
                continue

            if nums[l] > 0:
                break

            m, r = l + 1, len(nums) - 1

            while m < r:
                match nums[l] + nums[m] + nums[r]:
                    case s if s == 0:
                        res.append([nums[l], nums[m], nums[r]])
                        while m < r and nums[m] == res[-1][1]:
                            m += 1

                        while m < r and nums[r] == res[-1][2]:
                            r -= 1

                    case s if s < 0:
                        m += 1
                    case s if s > 0:
                        r -= 1


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
