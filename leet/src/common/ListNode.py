from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        next_repr = "" if self.next is None else str(self.next)
        return f"{self.val} + {next_repr}"

    def __eq__(self, __value):
        return super().__eq__(__value)


def to_linked_list(the_list: list[int]) -> Optional[ListNode]:
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
