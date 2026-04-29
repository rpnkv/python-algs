from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy = TreeNode(10, left=root)

        def find_parent(target: int):
            parent = dummy

            while parent:
                if parent.left and parent.left.val == target:
                    return parent, parent.left

                if parent.right and parent.right.val == target:
                    return parent, parent.right

                if target < parent.val:
                    parent = parent.left
                else:
                    parent = parent.right

            return parent, None

        parent, target = find_parent(key)

        if not target:
            return dummy.left


        # if removing node has no children
        if not target.left and not target.right:
            if parent.left.val == key:
                parent.left = None
                return dummy.left
            elif parent.right.val == key:
                parent.right = None
                return dummy.left

        def substitute(parent, target_val, target_node):
            if parent.left.val == target_val:
                parent.left = target_node
            else:
                parent.right = target_node

        # if removing node has 1 child (simple substitution resolution)
        if not target.left or not target.right:
            if target.left:
                substitute(parent, key, target.left)
                return dummy.left
            else:
                substitute(parent, key, target.right)
                return dummy.left

        raise NotImplementedError
