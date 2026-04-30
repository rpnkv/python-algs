from typing import Optional

from common.list_node import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowptr = head
        fastptr = head

        while fastptr is not None and fastptr.next is not None:

            fastptr = fastptr.next.next

            slowptr = slowptr.next

        return slowptr