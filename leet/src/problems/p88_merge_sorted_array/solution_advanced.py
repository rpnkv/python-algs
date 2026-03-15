from typing import List


class Solution:
    def merge(self, nums1: List[int],
              m: int,
              nums2: List[int],
              n: int
              ) -> None:
        # 1. 'vacant' initially points to the last element of the 'nums1'
        # 2. candidate1, candidate2 both point to m and n respectively
        # while candidate1 and candidate2 are greater or equal to 0, loop and insert greater element into vacant
        # position
        # 3. if 'candidate1' has ended first -- copy remaining 'nums2' values to vacant positions
        # if n == 0:
        #     return
        #
        # if m == 0:
        #     nums1[0:n] = nums2[0:n]
        #     return

        vacant = len(nums1) - 1
        candidate1 = m - 1
        candidate2 = n - 1

        while candidate1 >= 0 and candidate2 >= 0:
            if nums1[candidate1] > nums2[candidate2]:
                nums1[vacant] = nums1[candidate1]
                candidate1 -= 1
            else:
                nums1[vacant] = nums2[candidate2]
                candidate2 -= 1

            vacant -= 1

        if candidate1 < 0:
            nums1[0:vacant+1] = nums2[0:vacant+1]

        return
