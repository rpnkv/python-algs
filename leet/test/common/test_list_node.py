from common.list_node import ListNode, to_linked_list


def test_eq_success():
    ln1 = ListNode(2)
    ln2 = ListNode(2)

    assert ln1 == ln2
    assert ln1 is not ln2


def test_eq_failure():
    ln1 = ListNode(2)
    ln2 = ListNode(3)

    assert ln1 != ln2


def test_nested_equality_equal_depth():
    ln3 = ListNode(val=3)

    ln1 = ListNode(val=2, next=ln3)
    ln2 = ListNode(val=2, next=ln3)

    assert ln1 == ln2

    ln4 = ListNode(val=4)
    ln2.next = ln4

    assert ln1 != ln2


def test_nested_equality_various_depth():
    ln2 = ListNode(2)

    ln1_1 = ListNode(1, next=ln2)
    ln1_2 = ListNode(1)

    assert ln1_1 != ln1_2


def test_list_node_from_array_construction():
    ln2 = ListNode(2)
    ln1 = ListNode(1, next=ln2)
    ln0 = ListNode(0, next=ln1)

    assert ln0 == to_linked_list([*range(3)])
    assert ln0 != to_linked_list([*range(2)])
    assert ln0 != to_linked_list([*range(4)])
