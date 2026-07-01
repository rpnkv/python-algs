class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            if n & 1:
                count += 1
            n >>= 1

        return count

if __name__ == "__main__":
    cases = [
        (0b101, 2, "case 1"),
        (0b111, 3, "case 2"),
        (0b000, 0, "case 3"),
    ]

    for incoming, expected_outcome, case_id in cases:
       actual_outcome = Solution().hammingWeight(incoming)

       if actual_outcome != expected_outcome:
           print(f"Failed case {case_id}. In: {bin(incoming)}, out: {actual_outcome}")
       else:
           print(f"Case {case_id} passed")