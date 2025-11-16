from common.list_node import to_linked_list
from hard.p23.input_generator import produce_full


def test_test_data_generator_equal_lists_length():
    test_data = produce_full(30, 10, 0)
    expected_first_list = to_linked_list([*range(0, 9 + 1)])
    expected_second_list = to_linked_list([*range(10, 19 + 1)])
    expected_third_list = to_linked_list([*range(20, 29 + 1)])

    assert test_data[0] == expected_first_list
    assert test_data[1] == expected_second_list
    assert test_data[2] == expected_third_list

    assert (len(test_data) == 3)


def test_test_data_generator_NOT_equal_lists_length():
    test_data = produce_full(15, 10, 0)

    expected_first_list = to_linked_list([*range(0, 9 + 1)])
    expected_second_list = to_linked_list([*range(10, 15)])

    assert test_data[0] == expected_first_list
    assert test_data[1] == expected_second_list

    assert (len(test_data) == 2)
