class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = []

        for c in s:
            c = c.upper()
            if c.isdigit() or c.isalpha():
                newStr+=c


        for a,b in zip(newStr, reversed(newStr)):
            if a != b:
                return False

        return True

