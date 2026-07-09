class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ln_max = 0

        chars = {}

        def reload_freq():
            mfc, fr = "a", 0
            for mfc_candidate, f_candidate in chars.items():
                if f_candidate > fr:
                    mfc, fr = mfc_candidate, f_candidate

            return (mfc, fr)

        for r, c in enumerate(s):
            if c not in chars:
                chars[c] = 0
            chars[c] += 1

            most_freq_char, freq = reload_freq()

            while freq + k >= r - l:
                to_remove_char = s[l]
                chars[to_remove_char] -=1
                l+=1
                most_freq_char, freq = reload_freq()

            ln_max = max(ln_max, r - l + 1)

        return ln_max




if __name__ == "__main__":
    cases = [
        ("XYYX", 2, 4, "ex 1"),
        ("AAABABB", 1, 5, "ex 2")
    ]

    sol = Solution()

    for inp1, inp2, exp, case_id in cases:
        act = sol.characterReplacement(inp1, inp2)

        assert act == exp, f"failed case {case_id} act/exp: {act}/{exp}"
