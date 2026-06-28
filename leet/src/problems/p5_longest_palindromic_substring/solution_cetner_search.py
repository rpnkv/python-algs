# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # works for odd lists only
#         m = ""
#
#         def check_pal(l: int, r: int) -> tuple(bool, tuple[int, int]):
#             if l < 0 or r > len(s):
#                 return (False, (0, 0))
#
#             if (r - l > 1):
#                 is_pal = True
#             else:
#                 is_pal = False
#             pal_l, pal_r = l, r
#
#             while l >= 0 and r < len(s):
#                 if s[l] != s[r]:
#                     break
#                 is_pal = True
#                 pal_l, pal_r = l, r
#
#                 l -= 1
#                 r += 1
#
#             return (is_pal, (pal_l, pal_r))
#
#         for i in range(len(s)):
#             # check odd
#             l, r = i, i + 1
#             odd_check = check_pal(l, r)
#             if odd_check[0]:
#                 o_l, o_r = odd_check[1]
#                 if len(m) < (o_r - o_l + 1):
#                     m = s[o_l:o_r + 1]
#
#             # check even
#             l, r = i, i
#             even_check = check_pal(l, r)
#             if even_check[0]:
#                 e_l, e_r = even_check[1]
#                 if len(m) < (e_r - e_l + 1):
#                     m = s[e_l:e_r + 1]
#
#         return m

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         max_pal = (0, -1)  # когда такое не проканает?
#
#         def check_for_pal(l, r) -> tuple[bool, int, int]:
#             l_pal, r_pal = l, r
#             is_pal = l == r
#
#             while l >= 0 and r <= len(s) - 1:
#                 if s[l] == s[r]:
#                     is_pal = True
#                     l_pal, r_pal = l, r
#                 else:
#                     break
#
#                 l -= 1
#                 r += 1
#
#             return (is_pal, l_pal, r_pal)
#
#         for i, _ in enumerate(s):
#             is_pal, l_even, r_even = check_for_pal(i, i)
#             if is_pal and (max_pal[1] - max_pal[0]) < (r_even - l_even):
#                 max_pal = (l_even, r_even)
#
#             is_pal, l_odd, r_odd = check_for_pal(i, i + 1)
#             if is_pal and (max_pal[1] - max_pal[0]) < (r_odd - l_odd):
#                 max_pal = (l_odd, r_odd)
#
#         return s[max_pal[0]: max_pal[1] + 1]


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

if __name__ == "__main__":
    cases = [
        ("aacabdkacaa", ["aca"], "case 17"),
        ("abbc", ["bb"], "case 1"),
        ("a", ["a"], "case 3"),
        ("abcba", ["abcba"], "full centered"),
        ("abcde", [c for c in "abcde"], "no palindromes"),
        ("abade", ["aba"], "1-started"),
        ("acded", ["ded"], "3-started"),
        ("abbc", ["bb"], "example 2"),
    ]

    sol = Solution()

    for inc, exp_outc, case_id in cases:
        act_outc = sol.longestPalindrome(inc)

        if not act_outc in exp_outc:
            print(f"Failed case '{case_id}. Exp: {exp_outc}, act: {act_outc}")
        else:
            print(f"Succeeded case '{case_id}' succeeded.")
