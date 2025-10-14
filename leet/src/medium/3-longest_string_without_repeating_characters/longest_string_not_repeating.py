class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        max_length = 0
        current_substring = set()
        left = 0

        right = 0
        while right != len(s):
            letter = s[right]

            if letter not in current_substring:
                current_substring.add(letter)
                right += 1
                if max_length < len(current_substring):
                    max_length = len(current_substring)
                continue
            else:
                while s[right] in current_substring:
                    current_substring.remove(s[left])
                    left += 1

                current_substring.add(s[right])
                right += 1

        return max_length


def check(string: str, expected_length: int) -> None:
    length = Solution.length_of_longest_substring(string)
    assert length == expected_length, f'failed for {string}, expected {expected_length}, got {length}'


def main():
    check('abcabcbb', 3)
    check('pwwkew', 3)
    check('dvdf', 3)
    check('cdd', 2)


if __name__ == "__main__":
    main()
