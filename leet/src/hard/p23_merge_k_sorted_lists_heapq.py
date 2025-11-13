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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Heapq-based solution, expected to work for MlogN.
        """

        import heapq
        pq = []

        for head in [head for head in lists if head is not None]:
            heapq.heappush(pq, head)

        while len(pq) != 0:
            current_smallest = heapq.heappop(pq)
            self._append_list_node(current_smallest)

            if current_smallest.next is not None:
                next_node = current_smallest.next
                heapq.heappush(pq, next_node)

        return self.head
