from typing import Optional

from common.list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:  ## 12 minutes
        current: ListNode = head

        while current and current.next:
            if current.val == current.next.val:
                next_non_duplicate = current.next.next

                while next_non_duplicate and next_non_duplicate.val == current.val:
                    next_non_duplicate = next_non_duplicate.next

                current.next = next_non_duplicate

            current = current.next

        return head
