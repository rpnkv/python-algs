# Свертка списка в диапазоны
#
# Дан список неотрицательных целых чисел, повторяющихся элементов в списке нет. Нужно преобразовать его в строку,
# сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"
# [1,2] => "1-2"
#
import pytest


def split(input_nums: list[int]) -> str:
    input_set = {*input_nums}

    heads = [head for head in input_set if (head - 1) not in input_set]

    ranges = []

    for head in heads:
        prob_tail = head

        while (prob_tail + 1) in input_set:
            prob_tail += 1

        ranges.append((head, prob_tail))

    str_segments = []

    for r1, r2 in ranges:
        if r1 == r2:
            str_segments.append(str(r1))
        else:
            str_segments.append(f"{r1}-{r2}")

    return ",".join(str_segments)


def split_2(input_nums: list[int]) -> str:
    input_sorted = sorted(input_nums)

    # current_seq_start = input_sorted[0]
    #
    # for index, num in enumerate(input_sorted):
    #     if index != len(input_sorted) - 2:
    #         if input_sorted[index + 1] != (num + 1):
    #             seqs.append((current_seq_start, num))
    #             current_seq_start = input_sorted[index + 1]
    #     else:
    #         seqs.append((current_seq_start, num))
    # current_len = 0
    # current_start = 0
    # for index, num in enumerate(input_sorted):
    #     if index == 0:
    #         continue
    #
    #     if input_sorted[index - 1] == num - 1:
    #         current_len += 1
    #     else:
    #         seqs.append((input_sorted[current_start], input_sorted[index - 1]))
    #         current_start = index
    #         current_len = 0

    seqs = []
    current_start = 0
    for index, num in enumerate(input_sorted):
        if index != 0:
            if (num - 1) != input_sorted[index - 1]:
                # if current value isn't subsequent -- terminate previous range, start new range
                seqs.append((current_start, index - 1))
                current_start = index
            else:
                pass

    last_index = len(input_sorted) - 1
    if current_start == last_index:
        seqs.append((current_start, current_start))
    else:
        seqs.append((current_start, last_index))

    str_segments = []
    for r1, r2 in seqs:
        if r1 == r2:
            str_segments.append(str(input_sorted[r1]))
        else:
            str_segments.append(f"{input_sorted[r1]}-{input_sorted[r2]}")

    return ",".join(str_segments)


@pytest.mark.parametrize(
    argnames=["input_nums", "expected_output"],
    argvalues=[
        ([1, 4, 5, 2, 3, 9, 8, 11, 0], "0-5,8-9,11"),
        ([1, 4, 3, 2], "1-4"),
        ([1, 4], "1,4"),
        ([1, 4, 5, 2, 3, 9, 8, 11, 0], "0-5,8-9,11"),
    ]
)
def test_1(input_nums, expected_output):
    assert split(input_nums) == expected_output


@pytest.mark.parametrize(
    argnames=["input_nums", "expected_output"],
    argvalues=[
        ([1, 4, 5, 2, 3, 9, 8, 11, 0], "0-5,8-9,11"),
        ([1, 4, 3, 2], "1-4"),
        ([1, 4], "1,4"),
        ([1, 4, 5, 2, 3, 9, 8, 11, 0], "0-5,8-9,11"),
    ]
)
def test_2(input_nums, expected_output):
    assert split_2(input_nums) == expected_output
