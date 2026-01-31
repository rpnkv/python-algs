import sys
from typing import List, Optional

from common.list_node import ListNode


class Solution:
    """
    Naive solution for leetcode's task #23 "Merge K sorted lists".
    """

    head: Optional[ListNode] = None
    tail: Optional[ListNode] = None

    def _append_list_node(self, list_node: ListNode):
        if self.head is None:
            self.head = ListNode(list_node.val)
            self.tail = self.head
        else:
            new_tail = ListNode(list_node.val)
            self.tail.next = new_tail
            self.tail = new_tail

    def mergeKLists(self, input_lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Iterates over the whole list, until, at least, one sublist is not empty.

        Each iteration involves two operations, iterating over whole list elements (2N):
        - look for the smallest element value;
        - fetch all smallest elements and append them to a final list.


        """
        has_non_empty_lists = True
        lists = [head for head in input_lists]
        self.head = None
        self.tail = None

        while has_non_empty_lists:
            current_min = sys.maxsize
            has_non_empty_lists = False

            for nested_list in lists:
                if nested_list is not None:
                    has_non_empty_lists = True
                    if nested_list.val < current_min:
                        current_min = nested_list.val

            for index, nested_list in enumerate(lists):
                if nested_list is not None:
                    if nested_list.val == current_min:
                        self._append_list_node(nested_list)
                        lists[index] = nested_list.next

        return self.head
