class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # concepts
        # 1. iterate to first char, present in t using while loop
        # 2. we can now expand our window
        # 1.
        l = r = 0
        allowed_set = set(t)
        window_chars = {}

        res = ""
        win = ""

        while l < len(s) and s[l] not in t:
            l += 1

        # 2.
        for r in range(l, len(s)):
            char = s[r]
            if char in allowed_set:
                if char not in window_chars:

                else:
                    if s[l] == char:
                        l += 1
                        while s[l] not in allowed_set:
                            l += 1

            if len(window_set) == len(allowed_set):
                if res == "":
                    res = s[l: r + 1]
                    continue

                elif len(res) > (r - l + 1):
                    res = s[l: r + 1]
                    continue

            win = s[l: r+ 1]

        return res


if __name__ == "__main__":
    cases = [
        ("OUZODYXAZV", "XYZ", "YXAZ", "lc ex 1"),
        ("X", "XY", "", "lc ex 2"),
        ("ADOBECODEBANC", "ABC", "BANC", "lc case 8"),
    ]
    sol = Solution()
    for i1, i2, expected, case_id in cases[2:]:
        actual = sol.minWindow(i1, i2)
        assert actual == expected, f"case {case_id} failed: {expected}/{actual}"
