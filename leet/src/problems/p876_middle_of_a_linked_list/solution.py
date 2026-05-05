from typing import Optional

from common.list_node import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
