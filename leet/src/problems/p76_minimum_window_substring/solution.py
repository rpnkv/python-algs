class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""

        l = 0
        win_set = set()

        for r, c in enumerate(s):
            if not win_set:
                l = r

            if c in t:
                win_set.add(c)

            if win_set == set(t):
                if r - l - 1 < len(res) or res == "":
                    res = s[l:r + 1]

                win_set.remove(s[l])
                l += 1

                while s[l] not in win_set and l != r:
                    l += 1

        return res

if __name__ == "__main__":
    cases = [
        ("OUZODYXAZV", "XYZ", "YXAZ", "lc ex 1"),
        ("X", "XY", "", "lc ex 2"),
        ("ADOBECODEBANC", "ABC", "BANC", "lc case 8"),
        #("aa", "aa", "aa", "lc case 12"),
    ]
    sol = Solution()
    for i1, i2, expected, case_id in cases:
        actual = sol.minWindow(i1, i2)
        assert actual == expected, f"case {case_id} failed: {expected}/{actual}"
    print("All passed")