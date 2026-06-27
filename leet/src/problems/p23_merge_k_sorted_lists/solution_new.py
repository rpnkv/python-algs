# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from functools import reduce
from typing import List, Optional

from common.list_node import ListNode


class Solution:
    @staticmethod
    def linked_list_generator(head):
        current = head
        while current is not None:
            yield current
            current = current.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = heapq.merge(*[Solution.linked_list_generator(l) for l in lists], key=lambda k: k.val)

        head = tail = ListNode()

        for node in merged:
            tail.next = node
            tail = tail.next

        return head.next

        #return reduce(lambda acc, new: ListNode(new, acc), i, ListNode())


if __name__ == "__main__":
    cases = [
        (
            [ListNode(1), ListNode(2), ListNode(3)], ListNode.to_linked_list([1, 2, 3]), "case 1"
        )
    ]

    sol = Solution

    for incoming, expected_outcome, case_id in cases:
        actual_outcome = Solution().mergeKLists(lists=incoming)

        if actual_outcome != expected_outcome:
            print("FAILED")
        else:
            print("SUCCEEDED")
