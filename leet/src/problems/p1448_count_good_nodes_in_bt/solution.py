from common.tree_node import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode, parent:int =- pow(10,6)) -> int:
        rt = 1 if root and root.val >= parent else 0

        if root.left:
            l = self.goodNodes(root.left, max(root.val, parent))
        else:
            l = 0

        if root.right:
            r = self.goodNodes(root.right, max(root.val, parent))
        else:
            r = 0

        return r + l + rt
