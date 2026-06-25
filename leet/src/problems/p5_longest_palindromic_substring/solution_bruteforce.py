class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = ""

        def check(candidate: str) -> bool:
            for c1, c2 in zip(candidate, reversed(candidate)):
                if c1 != c2:
                    return False

            return True

        for i in range(len(s)):
            for j in range(i, len(s)):
                candidate = s[i: j + 1]
                if check(candidate):
                    if len(candidate) > len(max_pal):
                        max_pal = candidate

        return max_pal


if __name__ == "__main__":
    cases = [
        ("babad", ["bab", "aba"], "Example1"),
        ("cbbd", ["bb"], "Example2"),
    ]

    sol = Solution()

    print()
    for incoming, expected_outcome, case_id in cases:
        actual_outcome = sol.longestPalindrome(incoming)

        if actual_outcome not in expected_outcome:
            print(f"Failed {case_id}, actual: {actual_outcome}, expected:{expected_outcome}")
        else:
            print(f"Case {case_id} succeeded")
