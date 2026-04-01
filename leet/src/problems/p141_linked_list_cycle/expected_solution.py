from typing import Optional

from problems.p141_linked_list_cycle.naive_solution import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False


        if head.next == head:
            return True

        slow: ListNode = head

        if not head.next:
            return False

        fast: ListNode = head.next.next

        while fast and fast.next:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next

        return False

