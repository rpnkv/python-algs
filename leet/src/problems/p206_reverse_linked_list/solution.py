from typing import Optional

from common.list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        if not head.next.next:
            rev_head = head.next
            head.next = None
            rev_head.next = head
            return rev_head

        prev = None
        current = head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev