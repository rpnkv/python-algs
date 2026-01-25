# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from common.list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: ##13mins
        temp_head = ListNode(val=-101, next=head)

        previous: ListNode = temp_head
        current: ListNode = head

        while current and current.next:
            if current.val == current.next.val:
                temp_next = current.next.next

                while temp_next and temp_next.val == current.val:
                    temp_next = temp_next.next

                previous.next = temp_next
                current = temp_next
            else:
                previous = current
                current = previous.next

        return temp_head.next
