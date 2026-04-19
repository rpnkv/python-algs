class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0
        wovels = {'a', 'e', 'i', 'o', 'u'}

        curr_count = 0
        for i, chr in enumerate(s):
            count_incr = 1 if chr in wovels else 0

            if i >= k:
                count_decr = -1 if s[i-k] in wovels else 0
            else:
                count_decr = 0

            curr_count = curr_count + count_incr + count_decr
            max_count = max(max_count, curr_count)

        return max_count
