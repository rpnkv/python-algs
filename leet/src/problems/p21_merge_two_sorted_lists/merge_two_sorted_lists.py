from typing import Optional

from common.list_node import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res_dummy = ListNode()
        res_tail = res_dummy

        while list1 and list2:
            if list1.val < list2.val:
                res_tail.next = list1
                list1 = list1.next
            else:
                res_tail.next = list2
                list2 = list2.next

            res_tail = res_tail.next

        if list1 and not list2:
            res_tail.next = list1

        if list2 and not list1:
            res_tail.next = list2

        return res_dummy.next