from typing import List


class Solution:
    def merge(self, nums1: List[int],  # [0,0,0]
              m: int,  # 0
              nums2: List[int],  # [1,2,3]
              n: int  # 3
              ) -> None:
        """
        28.01.26 -- 13mins
        """

        # case 1 -- both empty: OK
        # case 2 -- right is empty: OK
        # case 3 -- left is empty: OK

        p1, p2, p = m - 1, n - 1, len(nums1) - 1 # -1, 2, 2

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

            p -= 1

        if p1 < 0:
            for i in range(p2 + 1): #[0,1,2]
                nums1[i] = nums2[i]
