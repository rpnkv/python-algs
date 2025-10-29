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
    def my_side_effect(gentle: bool = False):
        if gentle:
            return "Hello, sir!"
        else:
            return "I have absolutely no intention to communicate to you, rude!"

    dict = MagicMock()

    dict.some_function.side_effect = my_side_effect

    print()
    print(f"Response to gentle communication: '{dict.some_function(gentle=True)}'")
    print(f"Response to rude communication: '{dict.some_function(gentle=False)}'")


def test_mock_call_no_return_value():
    my_mock = Mock()

    my_mock(2, 3, 45)

    my_mock.assert_called_with(2, 3, 45)
