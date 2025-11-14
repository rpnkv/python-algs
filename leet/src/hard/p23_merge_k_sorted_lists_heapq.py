import heapq
import math
from typing import List, Optional

from common.list_node import ListNode


class Solution:
    """
    Heapq solution for leetcode's task #23 "Merge K sorted lists".
    """

    def __init__(self):
        self.head: Optional[ListNode] = ListNode(val=math.pow(10, 4) * -1 - 1, next=None)
        self.tail: Optional[ListNode] = self.head
        self.pq = []

    def _append_list_node(self, list_node: ListNode):
        if self.head is None:
            self.head = ListNode(list_node.val)
            self.tail = self.head
        else:
            new_tail = ListNode(list_node.val)
            self.tail.next = new_tail
            self.tail = new_tail

    @staticmethod
    def _wrap_tuple(list_node) -> tuple:
        return list_node.val, list_node

    @staticmethod
    def _unwrap_tuple(tuple_value: tuple) -> ListNode:
        return tuple_value[1]

    def _pq_has_more_elements(self) -> bool:
        return len(self.pq) != 0

    def _heappush(self, list_node: ListNode):
        heapq.heappush(self.pq, self._wrap_tuple(list_node))

    def _heappop(self) -> ListNode:
        return self._unwrap_tuple(heapq.heappop(self.pq))

    def _heapreplace(self, list_node: ListNode) -> ListNode:
        returning_tuple = heapq.heapreplace(self.pq, self._wrap_tuple(list_node))
        return self._unwrap_tuple(returning_tuple)

    def _min_nodes_next(self) -> ListNode:
        return self._unwrap_tuple(self.pq[0]).next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Heapq-based solution, expected to work for MlogN.
        """

        # put all the heads into list before continue
        for head in [head for head in lists if head is not None]:
            self._heappush(head)

        while self._pq_has_more_elements():
            min_nodes_next = self._min_nodes_next()

            if min_nodes_next is not None:
                # current linked_list isn't over so we
                appending_node = self._heapreplace(min_nodes_next)
            else:
                # current linked_list has no more elements so we just pop its value
                appending_node = self._heappop()

            self._append_list_node(appending_node)

        return self.head.next
