import pytest

from algs.fundamental.linked_list.iterate import iterate
from common.list_node import ListNode


@pytest.mark.parametrize(
    argnames=["head", "expected_nodes_list"],
    argvalues=[
        (None, []),
        (ListNode(1), [1]),
        (ListNode.to_linked_list([1, 2, 3]), [1, 2, 3]),
    ]
)
def test_iterate(head, expected_nodes_list):
    assert iterate(head) == expected_nodes_list
