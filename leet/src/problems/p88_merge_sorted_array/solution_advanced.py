from typing import List


class Solution:
    def merge(self, nums1: List[int],
              m: int,
              nums2: List[int],
              n: int
              ) -> None:
        vacant_index = len(nums1) - 1
        m_index = m - 1
        n_index = n - 1

        while m_index >= 0 and n_index >= 0:
            if nums1[m_index] > nums2[n_index]:
                nums1[vacant_index] = nums1[m_index]
                m_index -= 1
            else:
                nums1[vacant_index] = nums2[n_index]
                n_index -= 1

            vacant_index -= 1

        if n_index >= 0:
            the_slice = slice(0, n_index + 1)
            nums1[the_slice] = nums2[the_slice]