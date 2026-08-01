class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0] * n
            l, r = 0, 0

            for i in range(len(s)):
                curr_radii = 0
                while i - curr_radii > 0 and s[i - curr_radii] == s[i + curr_radii]:
                    curr_radii += 1
                curr_radii -= 1
                longest = i + curr_radii


            return p

        p = manacher(s)
        resLen, center_idx = max((v, i) for i, v in enumerate(p))
        resIdx = (center_idx - resLen) // 2
        return s[resIdx : resIdx + resLen]