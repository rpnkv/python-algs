from typing import List, Optional

from common.tree_node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        mid = len(nums) // 2

        return TreeNode(
            val=nums[mid],
            left=self.sortedArrayToBST(nums[:mid]),
            right=self.sortedArrayToBST(nums[mid + 1:]))
