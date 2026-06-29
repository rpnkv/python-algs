import math
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = math.inf

        for n in nums:
            if n > a:
                if n > b:  # a < b < n
                    return True
                else:  # a < n < b
                    b = n
            else:  # n <= a
                a = n

        return False


if __name__ == "__main__":
    cases = [
        # ([1, 2, -2, -1, 3], True, "my case 1"),
        ([1, 2, -1, 3], True, "my case 1"),
        # ([5,4,3,2,1], False, "example 2"),
        # (reversed([5,4,3,2,1]), True, "example 1"),
    ]

    for incoming, expected_outcome, case_id in cases:
        actual_outcome = Solution().increasingTriplet(incoming)

        match actual_outcome == expected_outcome:
            case True:
                print(f"Case {case_id} succeeded")
            case _:
                print(f"Case {case_id} failed: {actual_outcome}")
