class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        w_set = set('aeiou')

        l = w_cnt = w_max = 0

        for r, c in enumerate(s):
            w_cnt += int(c in w_set)

            if (r - l) == k:
                w_cnt -= int(s[l] in w_set)
                l += 1

            w_max = max(w_max, w_cnt)

        return w_max

