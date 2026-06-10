from typing import Optional

from common.list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nxt = None

        while head:
            cache = head.next
            head.next = nxt
            nxt = head
            head = cache

        return nxt