from typing import Optional

import pytest

from algs.fundamental.trees import tree_ops
from algs.fundamental.trees.tree_ops import are_equal
from common.tree_node import TreeNode


@pytest.mark.parametrize(
    ["left", "right", "expected_result"],
    [
        pytest.param(None, None, True, id="both are None"),
        pytest.param(None, TreeNode(), False, id="left is None"),
        pytest.param(TreeNode(), None, False, id="right is None"),
        pytest.param(TreeNode(), TreeNode(), True, id="both val is 0"),
        pytest.param(TreeNode(), TreeNode(1), False, id="left val is 0, right val is 1"),
    ]
)
def test_are_equal_single_level(left: Optional[TreeNode], right: Optional[TreeNode], expected_result: bool):
    assert are_equal(left, right) == expected_result


@pytest.mark.parametrize(
    ["left", "right", "expected_result"],
    [
        pytest.param(
            TreeNode(left=TreeNode(), right=TreeNode()),
            TreeNode(left=TreeNode(), right=TreeNode()),
            True,
            id="children are eq"
        ),
        pytest.param(
            TreeNode(left=TreeNode(1), right=TreeNode()),
            TreeNode(left=TreeNode(), right=TreeNode()),
            False,
            id="left child diff"
        ),
        pytest.param(
            TreeNode(left=TreeNode(), right=TreeNode(1)),
            TreeNode(left=TreeNode(), right=TreeNode()),
            False,
            id="right child diff"
        ),
        pytest.param(
            TreeNode(left=TreeNode(), right=TreeNode(1)),
            TreeNode(left=TreeNode(1), right=TreeNode()),
            False,
            id="both children diff"
        )
    ]
)
def test_are_equal_two_levels(left: Optional[TreeNode], right: Optional[TreeNode], expected_result: bool):
    assert are_equal(left, right) == expected_result


def test_sum():
    input_tree = TreeNode.from_level_order_array([1, 2, 3, 4, 5, 6, 7])  # 28

    assert tree_ops.get_tree_sum(input_tree) == 28


@pytest.mark.parametrize(
    argnames=["tree_array", "depth"],
    argvalues=[
        ([], 0),
        ([1], 1),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4, 5, 6, 7], 3),
    ],
    ids=["0", "1", "2", "3"]
)
def test_depth_recursive(tree_array: list[int], depth: int):
    input_tree = TreeNode.from_level_order_array(tree_array)  # 28

    assert tree_ops.get_tree_depth_recursive(input_tree) == depth


@pytest.mark.parametrize(
    argnames=["tree_array", "depth"],
    argvalues=[
        ([], 0),
        ([1], 1),
        ([1, 2, None], 2),
        #    ([1, 2, 3], 2),
        #    ([1, 2, 3, 4, 5, 6, 7], 3),
    ],
    ids=[
        "0",
        "1",
        "2",
        #    "2",
        #    "3"
    ]
)
def test_depth_iterative(tree_array: list[int], depth: int):
    input_tree = TreeNode.from_level_order_array(tree_array)

    assert tree_ops.get_tree_depth_iterative(input_tree) == depth
