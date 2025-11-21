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
        substr=set()
        max_len=0
        for index, character in enumerate(s):
            if character in substr:
                j = index - len(substr)
                while j < index:
                    substr.remove(s[j])
                    if s[j] == character:
                        j = index
                    j+=1

            substr.add(character)
            if len(substr) > max_len:
                max_len = len(substr)

        return max_len