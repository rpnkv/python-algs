class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        raise NotImplementedError
        while l < r:
            if s[l] in wovels:
                while s[r] not in wovels and r > l:
                    r -= 1

                s[l], s[r] = s[l], s[r]
                l += 1

        return s