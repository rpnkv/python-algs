import pytest

from common.tree_node import TreeNode
from problems.p450_delete_node_in_bst.solution import Solution

TEST_CASES = [
    pytest.param([1], 1, [], [], id="1 node, remove 1"),
    pytest.param([1], 2, [1], [], id="1 node, remove 1, no match"),
    pytest.param([2, 1, None], 2, [1], [], id="2 nodes, remove parent"),
    pytest.param([2, 1, None], 1, [2], [], id="2 nodes, remove child"),
    pytest.param([2, 1, 3], 1, [2, None, 3], [], id="3 nodes, remove left"),
    pytest.param([2, 1, 3], 3, [2, 1, None], [], id="3 nodes, remove right"),
    pytest.param([2, 1, 3], 3, [2, 1, None], [1, None, 2], id="3 nodes, remove parent"),
]


@pytest.mark.parametrize(
    ["source_tree_list", "key", "expected_answer_1_list", "expected_answer_2_list"], TEST_CASES
)
def test(source_tree_list: list[int], key: int, expected_answer_1_list: list[int],
         expected_answer_2_list: list[int]):
    source_tree = TreeNode.from_level_order_array(source_tree_list)

    actual_answer = Solution().deleteNode(source_tree, key)

    expected_answer_1 = TreeNode.from_level_order_array(expected_answer_1_list)
    expected_answer_2 = TreeNode.from_level_order_array(expected_answer_2_list)

    assert actual_answer == expected_answer_1 or actual_answer == expected_answer_2
