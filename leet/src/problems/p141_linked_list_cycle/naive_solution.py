from typing import Optional, Self


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

    @staticmethod
    def to_linked_list(the_list: list[int]) -> Optional[Self]:
        if len(the_list) == 1:
            return ListNode(val=the_list[0])
        elif len(the_list) == 0:
            return None

        head = ListNode(val=the_list[0])
        tail = head

        for value in the_list[1:]:
            tail_new = ListNode(val=value, next=None)
            tail.next = tail_new
            tail = tail_new

        return head



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """

        """
        if not head or not head.next:
            return False

        visited = set()

        while head:
            if head in visited:
                return True

            visited.add(head)
            head = head.next

        return False




