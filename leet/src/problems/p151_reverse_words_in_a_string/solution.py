# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = [*s.strip()]
#
#         def reverse_word(start:int, end:int):
#             while start < end:
#                 s[start], s[end] = s[end], s[start]
#                 start, end = start + 1, end - 1
#
#         l = 0
#         for r, c in enumerate(s):
#             if c == ' ':
#                 reverse_word(l, r - 1)
#                 l = r + 1
#
#
#         else:
#             reverse_word(l, len(s) - 1)
#
#         return "".join(reversed(s))
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []

        l = 0

        word = []
        for r, c in enumerate(s):
            if c != ' ':
                word.append(c)
            else:
                if word:
                    words.append(word)
                    word = []

        word = [*filter(lambda x: x.isalnum(), word)]

        if word:
            words.append(word)

        return " ".join(["".join(word) for word in reversed(words)])


if __name__ == "__main__":
    cases = [
        ("the sky is blue", "blue is sky the", "example 1"),
        ("  hello world  ", "world hello", "example 2"),
        ("a good   example", "example good a", "example 3"),
    ]

    for incoming, expected_outcome, case_id in cases:
        actual_outcome = Solution().reverseWords(incoming)

        if actual_outcome != expected_outcome:
            print(f"fail {actual_outcome} != {expected_outcome}")
        else:
            print(f"case {case_id} succeeded")
