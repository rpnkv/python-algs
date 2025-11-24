import pytest


def process_range(input_list: list[int]) -> list:
    output = []

    range_start = 0
    for index, num in enumerate(input_list):
        if index != 0:
            if (num - 1) != input_list[index - 1]:
                # if current value isn't subsequent -- terminate previous range, start new range
                output.append((range_start, index - 1))
                range_start = index
            else:
                pass

    last_index = len(input_list) - 1
    if range_start == last_index:
        output.append((range_start, range_start))
    else:
        output.append((range_start, last_index))

    return [(input_list[r1], input_list[r2]) for r1, r2 in output]


@pytest.mark.parametrize(
    argnames=["input_list", "expected_output_list"],
    argvalues=[
        ([1, 5, 6, 7, 8, 10, 12, 13, 15], [(1, 1), (5, 8), (10, 10), (12, 13), (15, 15)]),
        ([1, 2, 4], [(1, 2), (4, 4)]),  # cc1
        ([1, 3, 4], [(1, 1), (3, 4)]),  # cc2
        ([1, 3, 4, 6], [(1, 1), (3, 4), (6, 6)]),  # cc3
        ([1, 3, 6], [(1, 1), (3, 3), (6, 6)]),  # cc4
        ([1, 5, 6], [(1, 1), (5, 6)]),  # cc5
        ([1, 2, 6], [(1, 2), (6, 6)]),  # cc6
        ([0, 1, 2, 3, 4, 5, 8, 9, 11], [(0, 5), (8, 9), (11, 11)]),  # spcase
    ],
    ids=[
        "case 1",
        "cc1: continuous range at the beginning",
        "cc2: single value at the beginning",
        "cc3: range at the middle",
        "cc4: single value at the middle",
        "cc5: range at the end",
        "cc6: single value at the end",
        "special case"
    ]
)
def test(input_list, expected_output_list):
    assert process_range(input_list) == expected_output_list
