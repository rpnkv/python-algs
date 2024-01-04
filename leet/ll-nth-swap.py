# Definition for singly-linked list.
import queue
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        processing_node = self
        node_stack = []

        while processing_node is not None:
            node_stack.append(processing_node.val)
            processing_node = processing_node.next

        return str(node_stack)


def search_nodes(head: Optional[ListNode], searching_index: int) -> (ListNode, ListNode):
    processing_node = head
    last_values = queue.Queue(searching_index)

    left_node = None

    index = 0

    while processing_node is not None:
        if index == searching_index - 1:
            left_node = processing_node()

        if last_values.full():
            last_values.get()
        last_values.put(processing_node)
        processing_node = processing_node.next
        index += 1

    return left_node, last_values.get_nowait()


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes_stack = search_nodes(head, k)

        left_node = nodes_stack[0]
        right_node = nodes_stack[1]

        left_val = left_node.val

        left_node.val = right_node.val
        right_node.val = left_val

        return head


if __name__ == '__main__':
    # my_list = [1, 2, 3, 4, 5]
    # print(my_list[1:])
    #
    # print(my_list.pop())
    # print(my_list.pop())
    # print(my_list.pop())
    # print(my_list.pop())
    # print(my_list.pop())

    # inp = ListNode(val=1, next=None)
    # inp = ListNode(val=1, next=ListNode(val=2, next=None))
    inp = ListNode(val=1,
                   next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))
    # inp = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=None)))

    sol = Solution()
    print(sol.swapNodes(head=inp, k=2))
