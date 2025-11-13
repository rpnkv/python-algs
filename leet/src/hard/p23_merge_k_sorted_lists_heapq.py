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

        for index, head in enumerate([head for head in lists if head is not None]):
            heapq.heappush(pq, (head.val, index, head))

        while len(pq) != 0:
            min_index = pq[0][1]
            min_nodes_next = pq[0][2].next

            if min_nodes_next is not None:
                replacing_tuple = (min_nodes_next.val, min_index, min_nodes_next)
                self._append_list_node(heapq.heapreplace(pq, replacing_tuple)[2])
            else:
                self._append_list_node(heapq.heappop(pq)[2])

        return self.head
