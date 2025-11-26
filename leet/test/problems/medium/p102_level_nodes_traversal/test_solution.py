from common.tree_node import TreeNode
from problems.medium.p102_level_nodes_traversal.solution import Solution


def test():
    sol = Solution()
    input_tree = TreeNode(
        val=3,
        left=TreeNode(9),
        right=TreeNode(
            val=20,
            left=TreeNode(15),
            right=TreeNode(7)
        )
    )

    expected_output = [[3], [9, 20], [15, 7]]

    assert sol.levelOrder(input_tree) == expected_output
