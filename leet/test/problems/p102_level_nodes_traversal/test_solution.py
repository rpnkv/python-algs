from common.tree_node import TreeNode
from problems.medium.p102_level_nodes_traversal.solution import Solution

sol = Solution()

def test_1():
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


def test_2():
    sol = Solution()
    input_tree = TreeNode(
        val=1,
        left=TreeNode(2),
        right=None
    )

    expected_output = [[1], [2]]

    assert sol.levelOrder(input_tree) == expected_output


def test_3():
    root = TreeNode.from_level_order_array([1, 2, None, 3, None, 4, None, 5])
    output = sol.levelOrder(root)
    print(output)
