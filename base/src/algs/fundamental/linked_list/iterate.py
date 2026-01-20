from typing import Optional

from common.list_node import ListNode


def iterate(head: Optional[ListNode]) -> list[int]:
    res = []

    while head:
        res.append(head.val)
        head = head.next

    return res
