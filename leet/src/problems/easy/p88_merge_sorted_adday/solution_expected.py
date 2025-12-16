from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = nums1[:m]

        pos1 = pos2 = pos_out = 0

        while pos1 < m and pos2 < n:
            if temp[pos1] < nums2[pos2]:
                nums1[pos_out] = temp[pos1]
                pos_out += 1
                pos1 += 1
            else:
                nums1[pos_out] = nums2[pos2]
                pos_out += 1
                pos2 += 1

        while pos1 < m:
            nums1[pos_out] = temp[pos1]
            pos_out += 1
            pos1 += 1

        while pos2 < n:
            nums1[pos_out] = nums2[pos2]
            pos_out += 1
            pos2 += 1

