class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def is_proper_char(i: int) -> bool:
            try:
                return s[i].upper().isdigit() or s[i].upper().isalpha()
            except RuntimeError:
                print(f"Failed checking car at pos: {i}")



        while l != r:
            while not is_proper_char(l):
                l += 1
                if l == r:
                    return True

            while not is_proper_char(r):
                r -= 1
                if l == r:
                    return True

            if s[l].upper() != s[r].upper():
                return False
            else:
                l+=1
                r+=1

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