# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        processing_node = head
        node_stack = []

        while processing_node is not None:
            node_stack.append(processing_node)
            processing_node = processing_node.next

        if len(node_stack) == 1:
            return None
        elif len(node_stack) == 2:
            if n == 2:
                return node_stack.pop()
            else:
                head.next = None
                return head
        elif len(node_stack) == n:
            return node_stack[1:][0]
        else:
            top_value = None
            for i in range(n + 1):
                top_value = node_stack.pop()

            top_value.next = top_value.next.next

            return head


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    print(my_list[1:])
    #
    # print(my_list.pop())
    # print(my_list.pop())
    # print(my_list.pop())
    # print(my_list.pop())
    # print(my_list.pop())

    # inp = ListNode(val=1, next=None)
    # inp = ListNode(val=1, next=ListNode(val=2, next=None))
    # inp = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))
    inp = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=None)))

    sol = Solution()
    print(sol.removeNthFromEnd(head=inp, n=3))
