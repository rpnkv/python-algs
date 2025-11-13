from typing import Optional, Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def make_arg_value_new_head(self, new_head_value: int) -> Self:
        """
        Returns ListNode instance, containing "new_head_value" number, with current instance as a new ListNode.next
        value.
        """
        new_head = ListNode(new_head_value, self)
        return new_head

    def __str__(self):
        next_repr = "" if self.next is None else str(self.next)
        return f"{self.val} + {next_repr}"

    def __repr__(self):
        return f"ListNode(val={self.val}, next={repr(self.next)})"

    def __eq__(self, __value):
        if self.val != __value.val:
            return False

        if self.next is not None and __value.next is None:
            return False

        if self.next is None and __value.next is not None:
            return False

        return self.next == __value.next

    def __lt__(self, __value):
        return self.val < __value.val



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
