from typing import Optional, List

from common.list_node import to_linked_list, ListNode
from hard.p23_merge_k_sorted_lists_naive import Solution
from hard.test_case_generator import produce_full


def test_generic():
    function_input: List[Optional[ListNode]] = [
        to_linked_list([1, 2, 3]),
        to_linked_list([1, 2, 3]),
        to_linked_list([2, 3, 4])
    ]

    expected_output = to_linked_list(
        [1, 1,
         2, 2, 2,
         3, 3, 3,
         4]
    )

    sol = Solution()
    assert sol.mergeKLists(function_input) == expected_output


def test_empty():
    function_input: List[Optional[ListNode]] = [None]

    expected_output = None

    sol = Solution()
    assert sol.mergeKLists(function_input) == expected_output


def test_another_empty():
    function_input: List[Optional[ListNode]] = []

    expected_output = None

    sol = Solution()
    assert sol.mergeKLists(function_input) == expected_output

def test_load():
    function_input = produce_full()

    sol = Solution()
    output = sol.mergeKLists(function_input)

    output_length = 0

    while output is not None:
        output_length += 1
        output = output.next

    print()
    print(f"output length: {output_length}")