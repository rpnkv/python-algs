from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode], floor: int = -pow(2, 31), ceil=pow(2, 31) - 1) -> bool:
        if root is None:
            return True

        if root.left is not None and (root.left.val >= root.val or root.left.val < floor):
            return False

        if root.right is not None and (root.right.val <= root.val or root.right.val > ceil):
            return False

        return self.isValidBST(root.left, ceil=root.val) and self.isValidBST(root.right, floor=root.val)
