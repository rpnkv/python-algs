from typing import Optional, List

from common.list_node import ListNode
from problems.p23_merge_k_sorted_lists.p23_merge_k_sorted_lists_heapq import Solution
from problems.p23_merge_k_sorted_lists.test_p23_merge_k_sorted_lists_naive import create_input


def test_generic():
    function_input: List[Optional[ListNode]] = create_input()

    expected_output = ListNode.to_linked_list(
        [1, 1,
         2, 2, 2,
         3, 3, 3,
         4]
    )

    sol = Solution()
    assert sol.mergeKLists(function_input) == expected_output

    #checking if solution is idempotent
    assert function_input == create_input()
    assert sol.mergeKLists(function_input) == expected_output


def test_internal_list_empty():
    function_input: List[Optional[ListNode]] = [None]

    expected_output = None

    sol = Solution()

    actual_output = sol.mergeKLists(function_input)
    assert actual_output == expected_output


def test_external_list_empty():
    function_input: List[Optional[ListNode]] = []

    expected_output = None

    sol = Solution()
    assert sol.mergeKLists(function_input) == expected_output


def test_repeating_nums():
    function_input = [
        to_linked_list([1, 2, 2, 2, 3])
    ]

    expected_output = to_linked_list([1, 2, 2, 2, 3])
    sol = Solution()
    assert sol.mergeKLists(function_input) == expected_output
