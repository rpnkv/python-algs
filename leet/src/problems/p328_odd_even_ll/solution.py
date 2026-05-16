from typing import Optional

from common.list_node import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd_head = head
        even_head = head.next

        odd = head
        even = even_head

        while odd and even and even.next:
            odd.next = even.next
            even.next = even.next.next

            odd = odd.next
            even = even.next


        odd.next = even_head
        return odd_head