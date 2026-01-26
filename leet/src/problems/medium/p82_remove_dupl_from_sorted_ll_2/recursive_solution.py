from typing import Optional

from common.list_node import ListNode


class Solution:
    """
    Суть алгоритма, она в чём? Если число повторяется, мы должны от него избавиться.
    Минимальная "конфигурация" для такого решения -- где-то хранить предыдущее и как-то получить "следующее".
    """

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise NotImplementedError
        dummy_head = ListNode(val=-100, next=head)
        current: ListNode = dummy_head
        while current:
            ...

        return dummy_head.next
