class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev = {}
        ln_max = 0

        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                if c1 == c2:
                    if i - 1 not in prev:
                        prev[i] = 1
                    else:
                        prev[i] = prev[i - 1] + 1

                    ln_max = max(ln_max, prev[i])

        return ln_max


if __name__ == "__main__":
    cases = [
        ("abc", "adbc", 3, "my 1"),
        ("cat", "crabt", 3, "ex 1"),
    ]

    for inc1, inc2, exp, case_id in cases:
        act = Solution().longestCommonSubsequence(inc1, inc2)

        assert exp == act, f"failed case {case_id}: a/e:{act}/{exp}"
