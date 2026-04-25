import pytest

from common.tree_node import TreeNode
from problems.p98_validate_binary_search_tree.solution import Solution


@pytest.mark.parametrize(
    ["tree_as_loarr", "expected_result"],
    [
        pytest.param([2, 1, 3], True, id="Example 1"),
        pytest.param([5, 4, 6, None, None, 3, 7], False, id="Example 2"),
        pytest.param([45, 42, None, None, 44, 43, None, 41], False, id="Case 81"),
    ]
)
def test(tree_as_loarr: list[int], expected_result: bool):
    assert Solution().isValidBST(TreeNode.from_level_order_array(tree_as_loarr)) == expected_result
