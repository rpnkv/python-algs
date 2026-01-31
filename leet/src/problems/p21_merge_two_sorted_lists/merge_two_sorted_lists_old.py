# Definition for singly-linked list.
from typing import Optional

from common.list_node import ListNode, to_linked_list


class Solution:
    @staticmethod
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        head = None
        tail = None

        tail1 = list1
        tail2 = list2

        if tail1.val < tail2.val:
            head = tail1
            tail1 = tail1.next

            if tail1 is None:
                head.next = tail2
                return head

        else:
            head = tail2
            tail2 = tail2.next

            if tail2 is None:
                head.next = tail1
                return head

        head.next = None
        tail = head

        while tail1 is not None and tail2 is not None:
            if tail1.val < tail2.val:
                tail.next = ListNode(val=tail1.val)
                tail = tail.next
                tail1 = tail1.next
            else:
                tail.next = ListNode(val=tail2.val)
                tail = tail.next
                tail2 = tail2.next

        if tail1 is None:
            tail.next = tail2
        else:
            tail.next = tail1

        return head


def main():
    assert Solution.mergeTwoLists(list1=to_linked_list([1, 2, 4]), list2=to_linked_list([1, 3, 4])) == to_linked_list(
        [1, 1, 2, 3, 4, 4]
    )


if __name__ == "__main__":
    main()
