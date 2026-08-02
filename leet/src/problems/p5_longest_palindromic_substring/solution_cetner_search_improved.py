class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, -1
        t = "#" + "#".join(s) + "#"

        def expand(l: int, r: int) -> tuple[int, int]:
            while (l >= 0 and r < len(t) and
                   t[l] == t[r]):
                l, r = l - 1, r + 1

            return (l + 1, r - 1)

        for i, _ in enumerate(t):
            e1, e2 = expand(i, i)
            if e2 - e1 > end - start:
                start, end = e1, e2

        center_t = (end - start) // 2
        center = center_t // 2
        ln = (center_t - start) // 2

        # return s[start:end + 1]
        return s[center - ln:center + ln + 1]
