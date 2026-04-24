# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from common.tree_node import TreeNode


class Solution:

    def isSame(self, l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if not l and not r:
            return True

        if not l or not r:
            return False

        if l.val != r.val:
            return False

        return self.isSame(l.left, r.right) and self.isSame(l.right, r.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSame(root.left, root.right)
