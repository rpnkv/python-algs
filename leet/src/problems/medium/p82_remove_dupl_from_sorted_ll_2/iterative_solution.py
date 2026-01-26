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

        raise NotImplementedError


