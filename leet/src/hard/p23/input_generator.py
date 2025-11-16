import math

from common.list_node import to_linked_list, ListNode


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
