from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        current_level_nodes = [root] if root else []
        max_sum, max_sum_level = -pow(10, 6), 0
        current_level = 1

        while current_level_nodes:
            current_sum = 0
            next_level = []

            for node in current_level_nodes:
                current_sum += node.val

                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            if current_sum > max_sum:
                max_sum = current_sum
                max_sum_level = current_level

            current_level_nodes = next_level
            current_level += 1

        return max_sum_level
