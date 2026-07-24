class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lens = []

        def dfs(text1: str, text2: str) -> int:
            if len(text1) == 0 or len(text2) == 0:
                return 0
            m_l = 0
            for i, c1 in enumerate(text1):
                for j, c2 in enumerate(text2):
                    if c1 == c2:
                        max_len = dfs(text1[i + 1:], text2[j + 1:])
                        m_l = max(m_l, max_len + 1)
                        lens.append((i, j, 1 + max_len))

            return m_l

        dfs(text1, text2)
        l = [t[2]for t in lens]
        return max(l)


if __name__ == "__main__":
    cases = [
        ("abc", "adbc", 3, "my 1"),
        ("aebc", "adbc", 3, "my 2"),
        ("abec", "adbc", 3, "my 2"),
        ("cat", "crabt", 3, "ex 1"),
        ("crabt", "cat", 3, "ex 1 rev"),
        ("car", "crabt", 2, "case 4"),
    ]

    for inc1, inc2, exp, case_id in cases[0:]:
        act = Solution().longestCommonSubsequence(inc1, inc2)

        assert exp == act, f"failed case {case_id}: a/e:{act}/{exp}"
