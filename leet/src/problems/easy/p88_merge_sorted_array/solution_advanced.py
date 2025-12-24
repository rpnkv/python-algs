from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pos_1 = m - 1
        pos_2 = n - 1
        cursor = len(nums1) -1

        while pos_1 >= 0 and pos_2 >= 0:
            if nums1[pos_1] > nums2[pos_2]:
                nums1[cursor] = nums1[pos_1]
                pos_1 -= 1
            else:
                nums1[cursor] = nums2[pos_2]
                pos_2 -= 1

            cursor -= 1


        while pos_1 >= 0:
            nums1[cursor] = nums1[pos_1]
            pos_1 -= 1
            cursor -= 1

        while pos_2 >= 0:
            nums1[cursor] = nums2[pos_2]
            pos_2 -= 1
            cursor -= 1
