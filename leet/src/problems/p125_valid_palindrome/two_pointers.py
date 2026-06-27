class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not (s[l].isalpha() or s[l].isdigit()):
                l += 1

            while l < r and not (s[r].isalpha() or s[r].isdigit()):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1

        return True

if __name__ == "__main__":
    cases = [
        ("A man, a plan, a canal: Panama", True, "example 1"),
        ("race a car", False, "example 2"),
        (" ", True, "example 3"),
        (".,", True, "case 8"),
    ]

    sol = Solution()
    for i, e, c_id in cases:
        assert sol.isPalindrome(i) == e, c_id