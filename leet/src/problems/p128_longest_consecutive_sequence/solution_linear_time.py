class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()

        max_len = 1 if nums else 0

        for n in nums:
            if not (n - 1 in s):
                curr_len = 1
                while (n + 1) in s:
                    curr_len += 1
                    n += 1

                max_len = max(max_len, curr_len)


        return max_len

if __name__ == "__main__":
    cases = [
        ([1,2,3,4], 4, "my case 1")
    ]

    sol = Solution()

    print()
    for incoming, expected_outcome, case_id in cases:
        actual_outcome = sol.longestConsecutive(incoming)

        if actual_outcome != expected_outcome:
            print(f"case {case_id} failed. expected: {expected_outcome}, actual: {actual_outcome}.")
        else:
            print(f"case {case_id} succeeded")