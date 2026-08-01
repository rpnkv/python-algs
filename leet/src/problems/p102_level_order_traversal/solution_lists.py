class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvls = []

        curr = [root]

        while any(curr):
            curr_vals = []
            curr_children = []
            for node in curr:
                    if node:
                        curr_vals.append(node.val)
                        curr_children += [node.left, node.right]

            curr = curr_children
            lvls.append(curr_vals)

        return lvls