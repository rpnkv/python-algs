from typing import Optional, List

from common.list_node import to_linked_list, ListNode
from hard.p23_merge_k_sorted_lists_heapq import Solution


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


def test_repeating_nums():
    function_input = [
        to_linked_list([1, 2, 2, 2, 3])
    ]

    expected_output = to_linked_list([1, 2, 2, 2, 3])
    sol = Solution()
    assert sol.mergeKLists(function_input) == expected_output


def test_heapq_behavior():
    import heapq

    class TestNode:
        def __init__(self, val):
            self.val = val

    # Создаем ситуацию как в вашем алгоритме
    heap = []
    node1 = TestNode(5)
    node2 = TestNode(5)
    node3 = TestNode(5)

    heapq.heappush(heap, (5, 0, node1))
    print("После первого push:", heap)

    # Пытаемся сделать heapreplace как в вашем алгоритме
    try:
        heapq.heapreplace(heap, (5, 0, node2))
        print("heapreplace прошел успешно!")
        print("После heapreplace:", heap)
    except TypeError as e:
        print("Ошибка:", e)