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
    s = set(input_nums)
    res = []

    for n in input_nums:
        if n - 1 in s:
            continue
        else:
            start, end = n, n
            while end + 1 in s:
                end += 1

            res.append((start, end, end != start))

    return ",".join(f"{t[0]}-{t[1]}" if t[2] else f"{t[0]}" for t in res)


TEST_CASES = [
    pytest.param([1, 4, 5, 2, 3, 9, 8, 11, 0], "0-5,8-9,11"),
    pytest.param([1, 4, 3, 2], "1-4"),
    pytest.param([1, 4], "1,4"),
    pytest.param([3, 2, 1], "1-3"),
]


@pytest.mark.parametrize(
    ["input_nums", "expected_output"], TEST_CASES
)
def test(input_nums, expected_output):
    actual_output = split(input_nums)

    assert len(actual_output.split(",")) == len(expected_output.split(","))

    for e in expected_output.split(","):
        assert e in actual_output.split(",")
