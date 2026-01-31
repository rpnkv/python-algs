from typing import List


class Solution:
    @staticmethod
    def _check_if_one_letter_differs(current_word: str, checking_word: str) -> bool:
        letters_differ = 0

        current_letter_index = 0
        while current_letter_index < len(current_word) and letters_differ < 2:
            if current_word[current_letter_index] != checking_word[current_letter_index]:
                letters_differ += 1

            current_letter_index += 1

        return letters_differ == 1

    @staticmethod
    def _define_possible_routes(current_word: str, current_options: list[str]) -> list[str]:
        return [current_option for current_option in current_options if
                Solution._check_if_one_letter_differs(current_word, current_option)]

    @staticmethod
    def _search_recursively(current_word: str, target_word: str, word_list: List[str], current_steps: int) -> int:
        """
        Top level steps:
            1. Define possible routes for current word.
            2. Check if some possible routes returns non-zero.

        Implementation details:
            1. Define possible routes.
            Iterate over all possible routes and define those which match certain condition.

            2. Check if some possible routes return "true".



        """
        if len(word_list) == 0:
            return 0

        if current_word == target_word:
            return current_steps

        possible_routes = Solution._define_possible_routes(current_word, word_list)

        for possible_route in possible_routes:
            Solution._search_recursively()

        raise NotImplemented

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return self.search_recursively(beginWord, endWord, wordList, 0)
