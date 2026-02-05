import pytest


@pytest.mark.parametrize(
    argnames=["input_list", "expected_output_list"],
    argvalues=[
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4])
    ]
)
def test_solution(input_list: list[int], expected_output_list: list[int]):
    assert input_list[:len(expected_output_list)] == expected_output_list
