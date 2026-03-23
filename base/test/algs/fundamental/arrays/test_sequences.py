import pytest

from algs.fundamental.arrays.sequences import check_if_all_elements_are_equal



common_parametrize = pytest.mark.parametrize(
    argnames=["input_collection", "expected_result"],
    argvalues=[
        ([1], True),
        ([1, 1], True),
        ([1, 1, 1], True),
        ([1, 1, 1, 2], False),
        ([1, 1, 1, 2, 2], False),
        ([0, 1, 1, 1], False),
        ([0, 0, 1, 1, 1], False),
        ([1, 1, 0, 1, 1], False),
        ([1, 1, 0, 0, 1, 1], False),
    ]
)

@common_parametrize
def test_check_if_all_elements_are_equal(input_collection: list[int], expected_result: bool):
    assert check_if_all_elements_are_equal(input_collection) == expected_result
