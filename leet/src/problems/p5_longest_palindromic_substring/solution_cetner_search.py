class Solution:
    def longestPalindrome(self, s: str) -> str:
        # works for odd lists only

        m = ""

        for i in range(len(s)):
            l, r = i - 1, i + 1
            curr_len = 1

            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                curr_len += 2
                l -= 1
                r += 1

                if len(m) < (r - l + 1):
                    m = s[l:r+1]

        return m



if __name__ == "__main__":
    cases = [
        ("abcba", ["abcba"], "full centered"),
        ("abcde", [c for c in "abcde"], "no palindromes"),
        ("abade", ["aba"], "1-started"),
        ("acded", ["ded"], "3-started"),
    ]

    sol = Solution()

    for inc, exp_outc, case_id in cases:
        act_outc = sol.longestPalindrome(inc)

        if not act_outc in exp_outc:
            print(f"Failed case '{case_id}. Exp: {exp_outc}, act: {act_outc}")
        else:
            print(f"Succeeded case '{case_id}' succeeded.")
