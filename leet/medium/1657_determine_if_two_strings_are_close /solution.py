import functools
import sys
from typing import List


class Solution:
    @staticmethod
    def closeStrings(word1: str, word2: str) -> bool:
        return False


def main():
    assert Solution.closeStrings(word1="abc", word2="bca") is True
    assert Solution.closeStrings(word1="a", word2="aa") is True
    assert Solution.closeStrings(word1="cabbba", word2="abbccc") is True


if __name__ == "__main__":
    pass
