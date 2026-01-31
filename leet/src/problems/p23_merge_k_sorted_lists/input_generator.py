import math

from common.list_node import ListNode


def produce_full(elements_total: int = int(math.pow(10, 4)), elements_per_list: int = 500,
                 start_value: int = int(math.pow(10, 3) * -1)) -> list[ListNode]:
    """
    Produces full set of input
    """
    output = []

    full_lists_required = int(elements_total / elements_per_list)

    for list_index in range(0, full_lists_required):
        current_list_start_value = start_value + list_index * elements_per_list
        output.append(
            ListNode.to_linked_list([*range(current_list_start_value, current_list_start_value + elements_per_list)])
        )

    tail_length = elements_total - full_lists_required * elements_per_list

    if tail_length != 0:
        start_value = full_lists_required * elements_per_list
        output.append(
            ListNode.to_linked_list([*range(start_value, start_value + tail_length)])
        )

    return output
