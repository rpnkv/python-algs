class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0] * n
            # l, r = 0, 0

            for i in range(n):
                # if i < r:
                #     p[i] = min(r - i, p[l + (r - i)])

                while ((i + p[i] + 1 < n and i - p[i] - 1 >= 0) # while we're still inside the str
                        and t[i + p[i] + 1] == t[i - p[i] - 1]): # and inside the pal
                    p[i] += 1

                #if i + p[i] > r: # update boundaries
                #    l, r = i - p[i], i + p[i]
            return p

        pals = manacher(s)
        resLen, center_idx = max((v, i) for i, v in enumerate(pals))
        resIdx = (center_idx - resLen) // 2
        return s[resIdx: resIdx + resLen]
