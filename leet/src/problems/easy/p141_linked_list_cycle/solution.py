from typing import Optional

from common.list_node import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            return True

            slow = slow.next
            fast = fast.fast.next

        return False
