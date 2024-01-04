from typing import List


class Solution:

    @staticmethod
    def next_index(start: int, keep_checking: list[bool]) -> int:
        for i in range(start, len(keep_checking)):
            if keep_checking[i]:
                return i

        return -1

    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        max_len = max(list(map(len, strs)))

        keep_checking = []
        for i in range(0, len(strs)):
            keep_checking.append(True)

        substr = ""

        while all(keep_checking):

            index = Solution.next_index(0, keep_checking)
            current_letter = strs[index][len(substr)]
            for i in range(index, len(strs)):
                if keep_checking[i]:

        return "fl"


def main():
    assert Solution.longestCommonPrefix(["flight", "flower"]) == "fl"


if __name__ == "__main__":
    main()
