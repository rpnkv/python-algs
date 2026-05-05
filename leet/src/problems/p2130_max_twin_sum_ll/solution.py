from typing import Optional

from common.list_node import ListNode


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        pre_slow = None
        slow = head
        fast = head


        while fast and fast.next:
            fast = fast.next.next

            next = slow.next
            slow.next = pre_slow
            pre_slow = slow
            slow = next

        max_sum = 0

        while pre_slow:
            max_sum = max(pre_slow.val + slow.val, max_sum)

            pre_slow = pre_slow.next
            slow = slow.next
        return max_sum