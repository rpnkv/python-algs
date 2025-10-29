from unittest.mock import Mock, MagicMock

from common.ListNode import ListNode


def test_eq_success():
    ln1 = ListNode(2)
    ln2 = ListNode(2)

    assert ln1 == ln2


def test_eq_failure():
    ln1 = ListNode(2)
    ln2 = ListNode(3)

    assert ln1 != ln2


def test_another_day():
    ln1_internal = MagicMock()
    ln2_internal = MagicMock()

    ln1 = ListNode(next=ln1_internal)
    ln2 = ListNode(next=ln2_internal)

    print(ln1_internal)
    print(ln2_internal)

    ln1_internal.__eq__.assert_called_with(ln2_internal)


def test_mock_custom_behavior():
    dict = Mock()

    dict.side_effect(gentle=False).return_value = "I have absolutely no intention to communicate to you, rude!"
    dict.some_function(gentle=True).return_value = "Hello, sir!"

    print(dict.some_function(gentle=True))


def test_mock_call_no_return_value():
    my_mock = Mock()

    my_mock(2, 3, 45)

    my_mock.assert_called_with(2, 3, 45)
