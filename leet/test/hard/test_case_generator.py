import math

from common.list_node import ListNode, to_linked_list


def produce_full(total_elements: int = math.pow(10, 4), elements_per_list: int = 500,
                 start: int = math.pow(10, 3) * -1) -> list[ListNode]:
    """
    Produces full set of input
    """
    output = []

    full_lists_required = int(total_elements / elements_per_list)

    for i in range(0, full_lists_required):
        start = i * elements_per_list
        output.append(
            to_linked_list([*range(start, start + elements_per_list)])
        )

    tail_length = total_elements - full_lists_required * elements_per_list

    if tail_length != 0:
        start = full_lists_required * elements_per_list
        output.append(
            to_linked_list([*range(start, start + tail_length)])
        )

    return output


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

    assert(len(test_data) == 2)
