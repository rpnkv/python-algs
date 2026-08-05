# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         l = r = 0
#         allowed_set = set(t)
#         window_chars = {}
#
#         res = ""
#         win = ""
#
#         while l < len(s) and s[l] not in t:
#             l += 1
#
#         # 2.
#         for r in range(l, len(s)):
#             char = s[r]
#             if char in allowed_set:
#                 if char not in window_chars:
#
#                 else:
#                     if s[l] == char:
#                         l += 1
#                         while s[l] not in allowed_set:
#                             l += 1
#
#             if len(window_set) == len(allowed_set):
#                 if res == "":
#                     res = s[l: r + 1]
#                     continue
#
#                 elif len(res) > (r - l + 1):
#                     res = s[l: r + 1]
#                     continue
#
#             win = s[l: r+ 1]
#
#         return res
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        start, ln = 0, 0
        l = 0
        win, allowed = {}, Counter(t)

        def if_all_chars() -> bool:
            if win.keys() != allowed.keys():
                return False

            for win_key in win:
                if win[win_key] < allowed[win_key]:
                    return False
            return True

        for r, char in enumerate(s):
            if char in allowed:
                win[char] = 1 + win.get(char, 0)

            #while len(win) == len(allowed) and any((cnt > 1 for cnt in win.values())):
            while if_all_chars():
                if s[l] in allowed:
                    if win[s[l]] > allowed[s[l]]:
                        win[s[l]] -= 1
                    else:
                        break
                l += 1

            if if_all_chars():
                if ln == 0 or r - l + 1 < ln:
                    start, ln = l, r - l + 1

        return s[start: start + ln]


if __name__ == "__main__":
    cases = [
        ("OUZODYXAZV", "XYZ", "YXAZ", "lc ex 1"),
        ("X", "XY", "", "lc ex 2"),
        ("ADOBECODEBANC", "ABC", "BANC", "lc case 8"),
        ("aa", "aa", "aa", "lc case 12"),
    ]
    sol = Solution()
    for i1, i2, expected, case_id in cases[3:]:
        actual = sol.minWindow(i1, i2)
        assert actual == expected, f"case {case_id} failed: {expected}/{actual}"
