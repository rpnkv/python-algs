from typing import Optional

from algs.fundamental.trees.tree_ops import is_valid
from common.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return is_valid(root)
