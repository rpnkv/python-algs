from typing import Optional

from common.list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        26.01.26 -- 13 mins
        28.01.26 -- 10 mins
        """

        dummy_head = ListNode(val=-200, next=head)
        prev: ListNode = dummy_head  # dummy head
        current: ListNode = prev.next

        while current and current.next:
            if current.val == current.next.val:
                new_next = current.next
                while new_next and new_next.val == current.val:
                    new_next = new_next.next

                prev.next = new_next
                current = new_next
            else:
                prev = current
                current = prev.next

        return dummy_head.next
