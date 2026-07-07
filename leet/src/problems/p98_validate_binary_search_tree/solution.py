from typing import Optional

from algs.fundamental.trees.tree_ops import is_valid
from common.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode], floor=-pow(2,31) - 1, ceil = pow(2,31)) -> bool:
        if not root:
            return True

        if root.val < floor or root.val > ceil:
            return False

        return (
                self.isValidBST(root.left, floor=floor, ceil=root.val) and
                self.isValidBST(root.right, floor=root.val, ceil=ceil)
        )
