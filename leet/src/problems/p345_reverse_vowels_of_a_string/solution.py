class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        res = [" "] * len(s)
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        while l <= r:
            if s[l] in vowels:
                while s[r] not in vowels and r > l:
                    res[r] = s[r]
                    r -= 1

                res[l] = s[r]
                res[r] = s[l]
                r-=1

            else:
                res[l] = s[l]
            l += 1

        return "".join(res)