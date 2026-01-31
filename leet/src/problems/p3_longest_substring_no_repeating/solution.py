# class Solution:
#     @staticmethod
#     def length_of_longest_substring(s: str) -> int:
#         max_length = 0
#         current_substring = set()
#         left = 0
#
#         right = 0
#         while right != len(s):
#             letter = s[right]
#
#             if letter not in current_substring:
#                 current_substring.add(letter)
#                 right += 1
#                 if max_length < len(current_substring):
#                     max_length = len(current_substring)
#                 continue
#             else:
#                 while s[right] in current_substring:
#                     current_substring.remove(s[left])
#                     left += 1
#
#                 current_substring.add(s[right])
#                 right += 1
#
#         return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        max_len = 0
        for index, character in enumerate(s):
            if character in substr:
                j = index - len(substr)
                while s[j] != character:
                    substr.remove(s[j])
                    j += 1
            else:
                substr.add(character)
            if len(substr) > max_len:
                max_len = len(substr)

        return max_len

# str: abcabcbb
# idx: 01234567
# 1:
#   index/character: 0/a
#   if cond: false
#   ---
#   set: {a}
#   max_len: 0->1
# 2:
#   index/character: 1/b
#   if cond: false
#   ---
#   set: {a,b}
#   max_len: 1->2
# 3:
#   index/character: 3/c
#   if cond: false
#   ---
#   set: {a,b,c}
#   max_len: 2->3
# 4:
#   index/character: 4/a
#   if cond: true
#   j = 3-3=0
#   inner while loop (s[j] != 'a'):
#   1:
#
#
#
#
#   ---
#
#
#
#
