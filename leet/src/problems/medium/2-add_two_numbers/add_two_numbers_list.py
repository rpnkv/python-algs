# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = self.linkedListToArr(l1)
        lst2 = self.linkedListToArr(l2)

        max_length = len(lst1) if len(lst1) >= len(lst2) else len(lst2)

        self.adjustLength(lst1, max_length)
        self.adjustLength(lst2, max_length)

        num1 = self.listToNumber(lst1)
        num2 = self.listToNumber(lst2)

        total = num1 + num2

        num_list_normal = map(int, str(total))

        return self.arrayToLinkedList(num_list_normal)

    def linkedListToArr(self, l: Optional[ListNode]) -> list:
        lst = list()

        currentNode = l

        while (currentNode is not None):
            lst.append(currentNode.val)
            currentNode = currentNode.next

        return lst

    def adjustLength(self, list, bound):
        if len(list) < bound:
            for i in range(0, bound):
                if (i >= len(list)):
                    list.append(0)

    def listToNumber(self, lst) -> int:
        total = 0

        for i in range(0, len(lst)):
            total += lst[i] * pow(10, i)

        return total

    def arrayToLinkedList(self, list) -> Optional[ListNode]:
        list_head = None

        for v in list:
            if not list_head:
                list_head = ListNode(v, None)
            else:
                prev_head = list_head
                list_head = ListNode(v, next=prev_head)

        return list_head


def main():

    #l1 = ListNode(val=1, next=ListNode(val=7, next=ListNode(val=4, next=ListNode(val=1, next=None))))  # 741
    #l2 = ListNode(val=3, next=ListNode(val=6, next=ListNode(val=9, next=None)))  # 369

    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=9)))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=ListNode(val=9))))

    sol = Solution()
    k = sol.addTwoNumbers(l1, l2)

    num = sol.linkedListToArr(l=k)

    print(num)

if __name__ == "__main__":
    main()
