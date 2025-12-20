import pytest

from algs.fundamental.trees import tree_ops
from common.tree_node import TreeNode


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
        ([1,2, None], 2),
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
