from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        def most_left(root) -> TreeNode:
            return root

        def most_right(root) -> TreeNode:
            return root

        def search() -> TreeNode:
            node = root

            while node:
                if node.val == key:
                    break

                if key < node.val:
                    node = node.left
                else:
                    node = node.right
            return node

        removing_node, parent = search()

        if not removing_node:
            return root

        if not removing_node.left or not removing_node.right:
            if not removing_node.left:
                removing_node.val = removing_node.right.val
                removing_node.right = removing_node.right.right
                removing_node.left = removing_node.right.left
            else:
                removing_node.val = removing_node.left.val
                removing_node.right = removing_node.left.right
                removing_node.left = removing_node.left.left

        return root