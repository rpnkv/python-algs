from unittest.mock import Mock, NonCallableMagicMock, NonCallableMock

from common.list_node import ListNode


def test_eq_success():
    ln1 = ListNode(2)
    ln2 = ListNode(2)

    assert ln1 == ln2


def test_eq_failure():
    ln1 = ListNode(2)
    ln2 = ListNode(3)

    assert ln1 != ln2


def test_another_day():
    # spec_set = {"__eq__"}
    spec_set = {}

    ln1_internal = NonCallableMagicMock(spec_set=spec_set)
    ln2_internal = NonCallableMagicMock(spec_set=spec_set)
    ln3_internal = NonCallableMagicMock(spec_set=spec_set)

    ln1 = ListNode(next=ln1_internal)
    ln2 = ListNode(next=ln2_internal)

    print(ln1_internal)
    print(ln2_internal)

    ln1_internal.__eq__ = lambda self, other: other is ln2_internal

    #comparison_result = ln1_internal == ln2_internal

    print()
    print(f"ln1 eq to ln2: {ln1_internal == ln2_internal}")
    print(f"ln2 eq to ln3: {ln2_internal == ln3_internal}")

    #ln1_internal.__eq__.assert_called_with(ln2_internal)

    #print(f"Equity check result: {comparison_result}")


def test_try_to_raise_attribute_error():
    spec_set = ["some_function"]

    spec_mock = Mock(spec_set=spec_set)
    no_spec_mock = Mock()

    print(f"spec mock: {type(spec_mock)}")
    print(f"no spec mock: {type(no_spec_mock)}")
    # print(mock.some_function())


def test_mock_custom_behavior():
    def my_side_effect(gentle: bool = False):
        if gentle:
            return "Hello, sir!"
        else:
            return "I have absolutely no intention to communicate to you, rude!"

    dict = NonCallableMock()

    dict.some_function.side_effect = my_side_effect

    print()
    print(f"Response to gentle communication: '{dict.some_function(gentle=True)}'")
    print(f"Response to rude communication: '{dict.some_function(gentle=False)}'")


def test_mock_call_no_return_value():
    my_mock = Mock()

    my_mock(2, 3, 45)

    my_mock.assert_called_with(2, 3, 45)
