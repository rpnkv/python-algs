from typing import Optional

from common.list_node import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        reversed_head = head    # 1, 2, 3  4
        head = head.next        # 2, 3, 4, 5
        reversed_head.next = None

        while head: # 2, 3, 4, 5
            next_head = head.next   # 3, 4, 5, None
            head.next = reversed_head # 2.next = 1, 3.next = 2, 4.next = 3, 5.next = 4

            reversed_head=head      # 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5
            head = next_head        # 2 -> 3, 3 -> 4, 4 -> 5, 5 -> None

        return reversed_head