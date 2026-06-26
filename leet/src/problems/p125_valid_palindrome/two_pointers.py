class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.upper()

        def is_valid_char(i: int) -> bool:
            if s[i].isdigit() or s[i].isalpha():
                return True
            else:
                return False

        while l < r:
            while l < r and not is_valid_char(l):
                l += 1

            while r > l and not is_valid_char(r):
                r -= 1

            if s[l] != s[r]:
                return False

            l += 1
            r -=1


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