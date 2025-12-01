from typing import Optional

from common.list_node import ListNode, to_linked_list


class Solution:
    def mergeTwoLists(self,
                      list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        head: ListNode

        if list1.val < list2.val:
            head = ListNode(list1.val)
            list1=list1.next
        else:
            head = ListNode(list2.val)
            list2=list2.next

        tail=head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                next_tail=ListNode(list1.val)
                tail.next=next_tail
                list1=list1.next
                tail=next_tail
            else:
                next_tail=ListNode(list2.val)
                tail.next=next_tail
                tail=next_tail
                list2=list2.next

        if list1 is None and list2 is not None:
            tail.next=list2

        if list2 is None and list1 is not None:
            tail.next=list1

        return head


def main():
    sol = Solution()
    assert sol.mergeTwoLists(list1=to_linked_list([1, 2, 4]), list2=to_linked_list([1, 3, 4])) == to_linked_list(
        [1, 1, 2, 3, 4, 4]
    )


if __name__ == "__main__":
    main()
