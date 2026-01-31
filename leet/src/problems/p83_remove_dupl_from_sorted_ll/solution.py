from typing import Optional

from common.list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """

        26.01.26  12 minutes
        28.01.26  4 minutes
        """
        current: ListNode = head

        while current and current.next:
            if current.val != current.next.val:
                current = current.next
            else:
                temp_next: ListNode = current.next
                while temp_next and temp_next.val == current.val:
                    temp_next = temp_next.next

                current.next = temp_next

        return head
