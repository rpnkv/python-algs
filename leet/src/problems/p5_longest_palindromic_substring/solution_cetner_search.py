class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, -1

        def expand(l:int, r: int) -> tuple[int, int]:
            while (l >= 0 and r < len(s) and
                   s[l] == s[r]):
                l, r = l - 1, r + 1

            return (l + 1, r - 1)

        for i, _ in enumerate(s):
            # check even
            e1, e2 = expand(i, i)
            if e2 - e1 > end - start:
                start, end = e1, e2

            # check odd
            o1, o2 = expand(i, i + 1)
            if o2 - o1 > end - start:
                start, end = o1, o2

        return s[start:end + 1]