from os import read


class TreeCatalogue:

    @staticmethod
    def small():
        return TreeNode(1,
                        left=TreeNode(2,
                                      right=TreeNode(4)
                                      ),
                        right=TreeNode(
                            3
                        )
                        )

    @staticmethod
    def large():
        return TreeNode(6,
                        left=TreeNode(
                            2,
                            left=TreeNode(1),
                            right=TreeNode(4,
                                           left=TreeNode(3),
                                           right=TreeNode(5)
                                           )
                        ),
                        right=TreeNode(
                            7,
                            right=TreeNode(8,
                                           left=TreeNode(9))
                        )
                        )


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val},l={self.left},r={self.right})"


class PreOrder:

    def traverse(self, root: TreeNode):
        print(root.val, end=' ')
        if root.left is not None:
            PreOrder.traverse(self, root.left)
        if root.right is not None:
            PreOrder.traverse(self, root.right)


def main():
    PreOrder().traverse(TreeCatalogue.small())
    print()
    PreOrder().traverse(TreeCatalogue.large())


if __name__ == '__main__':
    # inp = input()
    # print(inp)
    main()
