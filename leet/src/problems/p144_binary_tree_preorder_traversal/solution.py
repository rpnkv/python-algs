from typing import Optional, List

from common.tree_node import TreeNode

#
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode], nodes=[]) -> List[int]:
#         if not root:
#             return []
#
#         nodes.append(root.val)
#         self.preorderTraversal(root.left, nodes=nodes)
#         self.preorderTraversal(root.right, nodes=nodes)
#
#         return nodes
#           doesn't work


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode], nodes=[]) -> List[int]:
        res = []


        def dfs(root: Optional[TreeNode]) -> None:
            if not root:
                return

            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res

if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [1, 2, 4, 5, 6, 7, 3, 8, 9], "example 2"),
    ]

    sol = Solution()
    for inc, outc, c_id in cases:
        act = sol.preorderTraversal(
            TreeNode.from_level_order_array(inc)
        )

        assert act == TreeNode.from_level_order_array(outc), f"failed for case {c_id}"
