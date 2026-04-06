from common.list_node import ListNode
from problems.p206_reverse_linked_list.solution import Solution


def test():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    Solution().reverseList(head)