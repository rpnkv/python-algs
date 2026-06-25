class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = max_len = curr_wovels = 0
        wovels = set(*[c for c in ['aeiou']])

        for r, c in enumerate(s):
            if c in wovels:
                curr_wovels += 1

            while (r - l) >= k:
                if s[l] in wovels:
                    curr_wovels -= 1

                l += 1

            max_len = max(max_len, curr_wovels)


        return max_len



