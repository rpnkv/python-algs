from typing import List, Optional

from common.tree_node import TreeNode


class Solution:

    def sortedArrayToBST(self, nums: List[int], start: int = 0, end: int = None) -> Optional[TreeNode]:
        the_end = len(nums) if not end else end

        mid =
