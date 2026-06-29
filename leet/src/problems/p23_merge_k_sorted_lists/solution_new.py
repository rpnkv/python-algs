import heapq
from typing import Optional, List

from common.list_node import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(l.val, i, l) for i, l in enumerate(lists)]

        heapq.heapify(h)

        res = tail = ListNode(val=-1001)

        while h:
            min_v, i, min_h = heapq.heappop(h)

            tail.next = min_h
            tail = tail.next

            if not min_h.next:
                pass
            else:
                v_next, h_next = min_h.next.val, min_h.next
                heapq.heappush(h, (v_next, i, h_next))

        return res.next


if __name__ == "__main__":
    cases = [
        (
            [
                ListNode.to_linked_list([1]),
                ListNode.to_linked_list([2]),
                ListNode.to_linked_list([3])
            ],
            ListNode.to_linked_list([1, 2, 3]),
            "my case 1"
        ),
        (
            [
                ListNode.to_linked_list([1, 2, 4]),
                ListNode.to_linked_list([1, 3, 5]),
                ListNode.to_linked_list([3, 6])
            ],
            ListNode.to_linked_list([1, 1, 2, 3, 3, 4, 5, 6]),
            "case 1"
        )
    ]

    sol = Solution

    for incoming, expected_outcome, case_id in cases:
        actual_outcome = Solution().mergeKLists(lists=incoming)

        if actual_outcome != expected_outcome:
            print("FAILED")
        else:
            print("SUCCEEDED")
