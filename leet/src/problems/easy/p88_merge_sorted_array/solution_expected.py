from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        copy = nums1[0:m]

        l1 = l2 = res = 0

        while l1 < m and l2 < n:
            if copy[l1] < nums2[l2]:
                nums1[res] = copy[l1]
                l1 += 1
            else:
                nums1[res] = nums2[l2]
                l2 += 1
            res += 1

        while l1 < m:
            nums1[res] = copy[l1]
            l1 += 1
            res += 1

        while l2 < n:
            nums1[res] = nums2[l2]
            l2 += 1
            res += 1
