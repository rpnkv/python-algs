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

def split4(input_nums: list[int]) -> str:
    s = set(input_nums)

    res = []

    for n in input_nums:
        if n - 1 in s:
            continue

        n_2 = n
        while n_2 + 1 in s:
            n_2 += 1

        if n == n_2:
            res.append((n,))
        else:
            res.append((n, n_2))

    return ",".join([str(r[0]) if len(r) == 1 else f"{r[0]}-{r[1]}" for r in res])




def splitX(input_nums: list[int]) -> str:
    s = set(input_nums)

    res = []

    for n in input_nums:
        if (n - 1) in s:
            continue
        else:
            val_0 = n
            val_1 = n
            while val_1 + 1 in s:
                val_1 += 1

            res.append((val_0, val_1) if val_0 != val_1 else (val_1,))

    return ",".join([str(val[0]) if len(val) == 1 else f"{val[0]}-{val[1]}" for val in res])


def split3(input_nums: list[int]) -> str:
    s = {num: True for num in input_nums}

    res = ""

    for n in input_nums:
        prev = n - 1
        if prev in s:
            continue
        else:
            s[n] = False
            s_tmp = str(n)
            n_tmp = n
            while n_tmp + 1 in s:
                n_tmp += 1
                s[n_tmp] = False

            if n_tmp != n:
                res += s_tmp + f"-{n_tmp},"
            else:
                res += s_tmp + ","

    return res[:-1]


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


TEST_CASES = [
    pytest.param([1, 4, 5, 2, 3, 9, 8, 11, 0], "0-5,8-9,11"),
    pytest.param([1, 4, 3, 2], "1-4"),
    pytest.param([1, 4], "1,4"),
    pytest.param([3, 2, 1], "1-3"),
]


@pytest.mark.parametrize(
    ["input_nums", "expected_output"], TEST_CASES
)
def test_3(input_nums, expected_output):
    actual_output = split3(input_nums)

    assert len(actual_output) == len(expected_output)

    for e in expected_output:
        assert e in actual_output


@pytest.mark.parametrize(
    ["input_nums", "expected_output"], TEST_CASES
)
def test_4(input_nums, expected_output):
    actual_output = split4(input_nums)

    assert len(actual_output.split(",")) == len(expected_output.split(","))

    for e in expected_output.split(","):
        assert e in actual_output.split(",")
