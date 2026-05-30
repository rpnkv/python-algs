import functools
import sys
from typing import List


class SolutionArch:

    @staticmethod
    def longest_common_prefix_not_optimal(strs: List[str]) -> str:
        shortest_string = min(sorted(strs, key=len, reverse=True))

        while shortest_string != "":
            if all(list(map(lambda x: x.startswith(shortest_string), strs))):
                return shortest_string
            else:
                shortest_string = shortest_string[:-1]

        return ""

    @staticmethod
    def longest_common_prefix_optimal(strs: List[str]) -> str:
        processing_row = 0

        while (True):
            prev_value = None
            for i in range(0, len(strs)):
                if len(strs[i]) <= processing_row:
                    return strs[i][: processing_row]
                else:
                    if prev_value is None:
                        prev_value = strs[i][processing_row]
                    else:
                        if prev_value != strs[i][processing_row]:
                            return strs[0][: processing_row]
            processing_row += 1

    @staticmethod
    def longest_common_prefix_super_optimal(strs: List[str]) -> str:
        for i, let in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if len(strs[j]) <= i:
                    return strs[0][:i]
                if strs[j][i] != let:
                    return strs[0][:i]

        return strs[0]


    # print(sys.getsizeof(["aaa", "aaa", "aaa", "aaa"]))    #
    # for v in [True, True, False, False]:
    #     print(id(v))
