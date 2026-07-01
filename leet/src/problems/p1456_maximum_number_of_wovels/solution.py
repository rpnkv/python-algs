class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        w_set = set(*[c for c in {'aeiou'}])

        l = w_cnt = w_max = 0

        for r, c in enumerate(s):
            if c in w_set:
                w_cnt += 1

            if (r - l) == k:
                if s[l] in w_set:
                    w_cnt -= 1
                l += 1

            w_max = max(w_max, w_cnt)

        return w_max

