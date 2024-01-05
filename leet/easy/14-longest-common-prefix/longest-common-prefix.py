from typing import List


class Solution:

    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        shortest_string = min(sorted(strs, key=len, reverse=True))

        while shortest_string != "":
            if all(list(map(lambda x: x.startswith(shortest_string), strs))):
                return shortest_string
            else:
                shortest_string = shortest_string[:-1]

        return ""


def main():
    assert Solution.longestCommonPrefix(["flight", "flower"]) == "fl"


if __name__ == "__main__":
    main()
