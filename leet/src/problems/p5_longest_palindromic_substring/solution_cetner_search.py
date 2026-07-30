class Solution:
    def longestPalindrome(self, s: str) -> str:
        p_l, p_r = 0, -1

        def check_pal(l:int, r:int) -> tuple[int,int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return (l + 1, r - 1)


        for i, _ in enumerate(s):
            # check odd
            o_l, o_r = check_pal(i, i + 1)
            if p_r - p_l < o_r - o_l:
                p_l, p_r = o_l, o_r

            # check even
            e_l, e_r = check_pal(i, i)
            if p_r - p_l < e_r - e_l:
                p_l, p_r = e_l, e_r

        return s[p_l: p_r + 1]