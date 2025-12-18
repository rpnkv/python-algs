import pytest

from common.tree_node import TreeNode


def _test_common_tree() -> TreeNode:
    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root_right = root.right

    root_right.left = TreeNode(15)
    root_right.right = TreeNode(7)

    return root


class _TestingTreeNode(TreeNode):
    def __eq__(self, __value):
        return self.val == __value.val


@pytest.mark.parametrize(
    argnames=["tn1", "tn2", "expected_result"],
    argvalues=[
        # 1lvl check
        (TreeNode(2), TreeNode(2), True),
        (TreeNode(2), TreeNode(3), False),
        # 2lvl check
        (
                TreeNode(2, left=_TestingTreeNode(3), right=_TestingTreeNode(4)),
                TreeNode(2, left=_TestingTreeNode(3), right=_TestingTreeNode(4)),
                True
        ),
        (
                TreeNode(2, left=_TestingTreeNode(3), right=_TestingTreeNode(3)),
                TreeNode(2, left=_TestingTreeNode(3), right=_TestingTreeNode(4)),
                False
        ),
        (
                TreeNode(2, left=_TestingTreeNode(4), right=_TestingTreeNode(4)),
                TreeNode(2, left=_TestingTreeNode(3), right=_TestingTreeNode(4)),
                False
        ),
        (
                TreeNode(2, left=_TestingTreeNode(3), right=None),
                TreeNode(2, left=_TestingTreeNode(3), right=_TestingTreeNode(4)),
                False
        ),
        (
                TreeNode(2, left=_TestingTreeNode(3), right=_TestingTreeNode(4)),
                TreeNode(2, left=_TestingTreeNode(3), right=None),
                False
        ),
        (
                TreeNode(2, left=None, right=_TestingTreeNode(4)),
                TreeNode(2, left=_TestingTreeNode(3), right=_TestingTreeNode(4)),
                False
        ),
        (
                TreeNode(2, left=_TestingTreeNode(3), right=_TestingTreeNode(4)),
                TreeNode(2, left=None, right=_TestingTreeNode(4)),
                False
        ),
    ],
    ids=[
        "1lvl equals",
        "1lvl differs",
        "2lvl equals full",
        "2lvl non-equals right full",
        "2lvl non-equals left full",
        "2lvl non-equals right partial 1",
        "2lvl non-equals right partial 2",
        "2lvl non-equals left partial 1",
        "2lvl non-equals left partial 2",
    ]
)
def test_equals_base(tn1, tn2, expected_result):
    if expected_result:
        assert tn1 == tn2
    else:
        assert tn1 != tn2


@pytest.mark.parametrize(
    argnames=["array_repr", "expected_tree"],
    argvalues=[
        ([1, 2, 3], TreeNode(1, left=TreeNode(2), right=TreeNode(3))),
        ([1, None, 2], TreeNode(val=1, right=TreeNode(2))),
        ([1, None, 2, None, None, 3, None], TreeNode(val=1, right=TreeNode(2, left=TreeNode(3))))
    ]
)
def test_from_level_order_array(array_repr: list[int], expected_tree: TreeNode):
    assert TreeNode.from_level_order_array(array_repr) == expected_tree


def test_to_level_order_array():
    root = _test_common_tree()
    expected_array = [3, 9, 20, None, None, 15, 7]

    assert root.to_level_order_array() == expected_array

    assert TreeNode(12).to_level_order_array() == [12]

    root.left = None
    root.right.left = None

    assert root.to_level_order_array() == [3, None, 20, None, None, None, 7]


def test_to_string_tree():
    root = _test_common_tree()
    print()
    print(root.to_string_tree())