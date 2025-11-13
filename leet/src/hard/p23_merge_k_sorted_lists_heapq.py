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

        # initial setup
        import heapq
        pq: list[(int, ListNode)] = []

        to_tuple = lambda list_node: (list_node.val, list_node)
        from_tuple = lambda tuple: tuple[1]

        for head in [head for head in lists if head is not None]:
            heapq.heappush(pq, to_tuple(head))

        while len(pq) != 0:
            appending_list_node: ListNode = pq[0][1]

            if appending_list_node.next is not None:
                next_tuple = to_tuple(appending_list_node.next)
                #heapq.heapreplace(pq, next_tuple)
                heapq.heappop(pq)
                heapq.heappush(pq, next_tuple)
            else:
                heapq.heappop(pq)

            self._append_list_node(appending_list_node)

        return self.head
