class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#" + "#".join(s) + "#"

        max_center, max_radi = 0, 0

        for i in range(len(t)):
            l, r, radi = i, i, 0

            while l >= 0 and r < len(t) and t[l] == t[r]:
                radi += 1
                l, r = i - radi, i + radi
            radi -= 1

            if radi > max_radi:
                max_center, max_radi = i, radi

        start_s = (max_center - max_radi) // 2
        end_s = start_s + max_radi

        return s[start_s:end_s]