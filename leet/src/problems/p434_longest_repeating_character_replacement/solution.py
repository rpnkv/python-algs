class Freq:
    def __init__(self):
        self.d = {}
        self.total = 0

    def append(self, c: str):
        if c not in self.d:
            self.d[c] = 0

        self.d[c] += 1
        self.total += 1

    def remove(self, c: str):
        if self.d[c] < 2:
            del self.d[c]
        else:
            self.d[c] -= 1

        self.total -= 1

    def count_others(self) -> int:
        d = self.d

        if len(d) == 1:
            return 0
        else:
            char, freq = "", 0
            for c1, f1 in d.items():
                if f1 > freq:
                    char, freq = c1, f1

            return self.total - freq

    def count_all(self) -> int:
        return self.total


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ln_max = 0

        freq = Freq()

        for r, c in enumerate(s):
            freq.append(c)

            while freq.count_others() > k:
                freq.remove(s[l])
                l += 1

            ln_max = max(ln_max, freq.count_all())

        return ln_max


if __name__ == "__main__":
    cases = [
        # ("XYY", 1, 3, "my 1"),
        # ("XXYY", 1, 3, "my 2"),
        ("XXXYY", 1, 4, "my 3"),
        # ("XYYX", 2, 4, "ex 1"),
        ("AAABABB", 1, 5, "ex 2")
    ]

    sol = Solution()

    for inp1, inp2, exp, case_id in cases:
        act = sol.characterReplacement(inp1, inp2)

        assert act == exp, f"failed case {case_id} act/exp: {act}/{exp}"
