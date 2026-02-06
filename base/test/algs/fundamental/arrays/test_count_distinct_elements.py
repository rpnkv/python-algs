import pytest

from algs.fundamental.arrays.count_distinct_elements import count_distinct_elements


@pytest.mark.parametrize(
    argnames=["input_array", "expected_count"],
    argvalues=[
        ([], 0),
        ([1], 1),
        ([1, 1, 1, 1], 1),
        ([1, 1, 1, 2], 2),
        ([1, 2, 2, 2], 2),
        ([1, 1, 1, 2, 2, 2], 2),
        ([1, 2], 2),
        ([1, 2, 3], 3),
    ]
)
def test_count_distinct_elements(input_array: list[int], expected_count: int):
    assert count_distinct_elements(input_array) == expected_count
