# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         if len(text1) < len(text2):
#             pass
#         else:
#             text1, text2 = text2, text1
#
#         ln_max = 0
#         max_lens = [0] * len(text1)
#         paths = [[] for _ in text1]
#
#         for i, chr1 in enumerate(text1):
#             for j, chr2 in enumerate(text2):
#                 if chr1 == chr2:
#                     paths[i].append(j)
#                     if i == 0:
#                         max_lens[i] = 1
#                     else:
#                         max_lens[i] = max(max_lens[:i]) + 1
#
#         return max(max_lens)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            pass
        else:
            text1, text2 = text2, text1

        ln_max = 0
        max_lens = [0] * len(text1)
        paths = []


        for j, chr2 in enumerate(text2):
             if text2[j] == text1[0]:
                 paths.append(j)

        for i in range(1, len(text1)):
            for

        # for i, chr1 in enumerate(text1):
        #     for j, chr2 in enumerate(text2):
        #         if chr1 == chr2:
        #             paths[i].append(j)
        #             if i == 0:
        #                 max_lens[i] = 1
        #             else:
        #                 max_lens[i] = max(max_lens[:i]) + 1

        return max(max_lens)

if __name__ == "__main__":
    cases = [
        ("abc", "adbc", 3, "my 1"),
        ("aebc", "adbc", 3, "my 2"),
        ("abec", "adbc", 3, "my 2"),
        ("cat", "crabt", 3, "ex 1"),
        ("crabt", "cat", 3, "ex 1 rev"),
        ("car", "crabt", 2, "case 4"),
    ]

    for inc1, inc2, exp, case_id in cases[5:]:
        act = Solution().longestCommonSubsequence(inc1, inc2)

        assert exp == act, f"failed case {case_id}: a/e:{act}/{exp}"
