from typing import Self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    def from_array(values: list[int]) -> Self:
        raise NotImplemented
