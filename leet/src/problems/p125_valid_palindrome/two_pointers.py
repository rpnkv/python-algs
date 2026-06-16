class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.upper()

        def check_letter(i: int) -> bool:
            if not s[i].isalpha() and not s[i].isdigit():
                return False
            return True

        while l < r:
            while not check_letter(l):
                l+=1

            while not check_letter(r):
                r-=1

            if s[l] != s[r]:
                return False

            l+=1
            r-=1

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