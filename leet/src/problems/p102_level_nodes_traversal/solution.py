from typing import Optional, List

from common.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        results = [[root.val]]

        global_parents = [root]

        while len(global_parents) != 0:
            current_children_nodes = []
            current_results = []

            for parent in global_parents:
                if parent.left is not None:
                    current_children_nodes.append(parent.left)
                    current_results.append(parent.left.val)

                if parent.right is not None:
                    current_children_nodes.append(parent.right)
                    current_results.append(parent.right.val)

            if len(current_results) != 0:
                results.append(current_results)
            global_parents = current_children_nodes

        return results
