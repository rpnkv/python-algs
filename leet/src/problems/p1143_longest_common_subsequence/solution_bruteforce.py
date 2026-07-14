class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ln_max = 0
        paths = [[]] * len(text1)

        for i, chr1 in enumerate(text1):
            for j, chr2 in enumerate(text2):
                if chr1 == chr2:
                    paths[i].append(j)

        return ln_max


if __name__ == "__main__":
    cases = [
        ("abc", "adbc", 3, "my 1"),
        ("aebc", "adbc", 3, "my 2"),
        ("abec", "adbc", 3, "my 2"),
        ("cat", "crabt", 3, "ex 1"),
        ("crabt", "cat", 3, "ex 1 rev"),
        ("crabt", "car", 2, "case 4"),

    ]

    for inc1, inc2, exp, case_id in cases[5:]:
        act = Solution().longestCommonSubsequence(inc1, inc2)

        assert exp == act, f"failed case {case_id}: a/e:{act}/{exp}"
