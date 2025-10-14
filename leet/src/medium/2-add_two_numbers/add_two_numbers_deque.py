# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val


class Solution:
    carry = 0

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer_head = None
        answer_tail = None
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            result = (0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + carry
            carry = result // 10

            result = result % 10

            if answer_tail is None:
                answer_tail = ListNode(val=result)
            else:
                answer_tail.next = ListNode(val=result)
                answer_tail = answer_tail.next

            if answer_head is None:
                answer_head = answer_tail

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return answer_head


def main():
    # l1 = ListNode(val=1, next=ListNode(val=7, next=ListNode(val=4, next=ListNode(val=1, next=None))))  # 741
    # l2 = ListNode(val=3, next=ListNode(val=6, next=ListNode(val=9, next=None)))  # 369

    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=9)))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=ListNode(val=9))))

    # l1 = ListNode(val=0)
    # l2 = ListNode(val=0)

    # l1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9,
    #                                                                                                   next=ListNode(
    #                                                                                                       val=9,
    #                                                                                                       next=ListNode(
    #                                                                                                           val=9)))))))
    # l2 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9))))

    sol = Solution()
    k = sol.addTwoNumbers(l1, l2)
    print(k)


if __name__ == "__main__":
    main()
