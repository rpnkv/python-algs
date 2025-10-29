from common.ListNode import to_linked_list, ListNode
from hard.p23_merge_k_sorted_lists_naive import Solution


def test_something():
    input = [
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



    #assert Solution.mergeKLists(input) == expected_output
    assert Solution.mergeKLists(input) == ListNode()
