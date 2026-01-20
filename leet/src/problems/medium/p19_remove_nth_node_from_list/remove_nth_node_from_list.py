from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        next_repr = "" if self.next is None else str(self.next)
        return f"{self.val} + {next_repr}"


class Solution:
    @staticmethod
    def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = n

        fast_pointer = head
        slow_pointer = head

        for i in range(0, n):
            fast_pointer = fast_pointer.next

        if fast_pointer is not None:
            while fast_pointer is not None and fast_pointer.next is not None:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next

            slow_pointer.next = slow_pointer.next.next
            return head
        else:
            return head.next


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


def main():
    # assert Solution.removeNthFromEnd(head=to_linked_list([1,2,3,4,5]), n=2) == [1,2,3,5]
    # assert Solution.removeNthFromEnd(head=to_linked_list([1]), n=1) == to_linked_list([])
    # assert Solution.removeNthFromEnd(head=to_linked_list([1,2]), n=1) == [1]
    assert Solution.removeNthFromEnd(head=to_linked_list([1, 2]), n=2) == [1]
    # Input: head = [1,2,3,4,5], n = 2
    # Output: [1,2,3,5]


if __name__ == "__main__":
    main()
