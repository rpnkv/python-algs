from typing import List, Optional

from common.list_node import ListNode


class Solution:
    """
    Heapq solution for leetcode's task #23 "Merge K sorted lists".
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

        # PQ components
        import heapq
        pq = []

        # list_nodes to tuple (PQ-supported elements) conversion methods so we won't make indexing etc mistakes
        value_index = 1
        wrap_tuple = lambda list_node: (list_node.val, list_node)
        unwrap_tuple = lambda tuple_value: tuple_value[value_index]

        # put all the heads into list before continue
        for head in [head for head in lists if head is not None]:
            heapq.heappush(pq, wrap_tuple(head))

        while len(pq) != 0:
            min_nodes_next = unwrap_tuple(pq[0]).next

            next_tail_tuple: tuple

            if min_nodes_next is not None:
                # current linked_list isn't over so we
                replacing_tuple = wrap_tuple(min_nodes_next)
                next_tail_tuple = heapq.heapreplace(pq, replacing_tuple)
            else:
                # current linked_list has no more elements so we just pop its value
                next_tail_tuple = heapq.heappop(pq)

            next_tail_list_node = unwrap_tuple(next_tail_tuple)
            self._append_list_node(next_tail_list_node)

        return self.head
