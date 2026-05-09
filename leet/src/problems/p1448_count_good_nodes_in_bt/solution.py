from common.tree_node import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        l = 1 if root.left and root.left.val < root.val else 0
        r = 1 if root.right and root.right.val < root.val else 0

        return r + l + self.goodNodes(root.left) + self.goodNodes(root.right)
