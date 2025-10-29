from unittest.mock import NonCallableMagicMock

from common.list_node import ListNode


def test_eq_success():
    ln1 = ListNode(2)
    ln2 = ListNode(2)

    assert ln1 == ln2


def test_eq_failure():
    ln1 = ListNode(2)
    ln2 = ListNode(3)

    assert ln1 != ln2


def test_nested_equality():
    ln1_internal = NonCallableMagicMock(spec_set=ListNode)
    ln2_internal = NonCallableMagicMock(spec_set=ListNode)
    ln3_internal = NonCallableMagicMock(spec_set=ListNode)

    ln1 = ListNode(val=2, next=ln1_internal)
    ln2 = ListNode(val=2, next=ln2_internal)
    ln3 = ListNode(val=2, next=ln3_internal)

    ln1_internal.__eq__ = lambda self, other: (other == ln2_internal)

    assert ln1 == ln2
    assert ln1 != ln3


