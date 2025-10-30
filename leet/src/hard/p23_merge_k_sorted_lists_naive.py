# Definition for singly-linked list.
import sys
from typing import List, Optional

from common.list_node import ListNode


class Solution:
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [nested_list for nested_list in lists if type(nested_list) is ListNode]
        while len(lists) > 0:
            current_min = sys.maxsize
            for nested_list in lists:
                if nested_list is not None:
                    if nested_list.val < current_min:
                        current_min = nested_list.val

            for index, nested_list in enumerate(lists):
                if len(nested_list) > 0 and nested_list.val == current_min:
                    self._append_list_node(nested_list)
                    lists[index] = nested_list.next

            lists = [nested_list for nested_list in lists if type(nested_list) is ListNode]

        return self.head
