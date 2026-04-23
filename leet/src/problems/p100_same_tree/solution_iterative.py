# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def check_level(self, p:list[TreeNode], q: list[TreeNode]) -> bool:
        if len(p) != len(q):
            return false

        for i in len(p):
            if p[i].val != p[q].val:
                return false

        return true

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list = [p] if p else []
        q_list = [q] if q else []



        while q and p
