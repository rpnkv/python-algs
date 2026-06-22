class Solution:
    def merge(self, nums1: List[int],
              m: int,
              nums2: List[int],
              n: int
              ) -> None:

        vacant, i_1, i_2 = len(nums1) - 1, m - 1, n - 1

        while i_1 >= 0 and i_2 >= 0:
            if nums1[i_1] > nums2[i_2]:
                nums1[vacant] = nums1[i_1]
                i_1-=1
            else:
                nums1[vacant] = nums2[i_2]
                i_2-=1


            vacant -= 1

        if i_2 >= 0:
            nums1[:vacant + 1] = nums2[:i_2 + 1]
