from typing import Optional

from problems.p141_linked_list_cycle.naive_solution import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
            Two iterators: slow and fast.

        """
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while fast.next and fast.next.next:
            fast = fast.next.next
            if slow == fast:
                return True
            slow = slow.next

        return False
