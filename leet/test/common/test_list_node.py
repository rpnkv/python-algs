from common.list_node import ListNode


def test_eq_success():
    ln1 = ListNode(2)
    ln2 = ListNode(2)

    assert ln1 == ln2
    assert ln1 is not ln2


def test_eq_failure():
    ln1 = ListNode(2)
    ln2 = ListNode(3)

    assert ln1 != ln2


def test_nested_equality_otherwise():
    ln3 = ListNode(val=3)

    ln1 = ListNode(val=2, next=ln3)
    ln2 = ListNode(val=2, next=ln3)

    assert ln1 == ln2

    ln4 = ListNode(val=4)
    ln2.next = ln4

    assert ln1 != ln2
