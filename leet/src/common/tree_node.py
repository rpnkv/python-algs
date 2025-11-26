from typing import Self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

    def __eq__(self, __value):
        current_level_equals = self.val == __value.val

        left_equals = (self.left is None and __value.left is None
                       ) or (
                              self.left is not None and __value.left is not None and self.left == __value.left)

        right_equals = (
                               self.right is None and __value.right is None
                       ) or (self.right is not None and __value.right is not None and self.right == __value.right)
        return current_level_equals and left_equals and right_equals

    @staticmethod
    def from_array(array_repr: list[int]) -> Self:
        if not array_repr or array_repr[0] is None:
            return None

        root = TreeNode(array_repr[0])
        queue = [root]
        i = 1

        while queue and i < len(array_repr):
            node = queue.pop(0)

            # Left child
            if i < len(array_repr) and array_repr[i] is not None:
                node.left = TreeNode(array_repr[i])
                queue.append(node.left)
            i += 1

            # Right child
            if i < len(array_repr) and array_repr[i] is not None:
                node.right = TreeNode(array_repr[i])
                queue.append(node.right)
            i += 1

        return root
