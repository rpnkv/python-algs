from typing import List, Optional

from common.tree_node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int], start: int = 0, end: int = None) -> Optional[TreeNode]:
        the_end = len(nums) - 1 if not end else end

        if start == the_end:
            return TreeNode(nums[start])

        mid = the_end + start // 2
        return TreeNode(
            nums[mid],
            self.sortedArrayToBST(nums, start, mid - 1),
            self.sortedArrayToBST(nums, mid + 1, the_end)
        )


