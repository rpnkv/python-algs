import math

from common.list_node import to_linked_list
from problems.hard.p23_merge_k_sorted_lists.input_generator import produce_full


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


def test_produce_single_list_10k_els():
    test_data = produce_full(elements_total=int(math.pow(10, 4)), elements_per_list=int(math.pow(10, 4)),
                             start_value=1)

    assert len(test_data) == 1
    linked_list_head = test_data[0]

    assert linked_list_head is not None
    assert linked_list_head.val == 1

    prev_value = 0
    while linked_list_head is not None:
        assert prev_value + 1 == linked_list_head.val

        prev_value = linked_list_head.val
        linked_list_head = linked_list_head.next

    assert prev_value == math.pow(10, 4)


def test_produce_two_lists_5k_els_each():
    elements_total = int(math.pow(10, 4))
    elements_per_list = int(elements_total / 2)

    test_data = produce_full(
        elements_total=elements_total, elements_per_list=elements_per_list, start_value=2
    )

    assert len(test_data) == 2
    assert len(test_data[0]) == elements_per_list
    assert len(test_data[1]) == elements_per_list


