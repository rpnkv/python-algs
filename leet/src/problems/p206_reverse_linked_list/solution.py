from typing import Optional

from common.list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None

        while head:
            nxt = head.next
            head.next = new_head
            new_head = head
            head = nxt

        return new_head
