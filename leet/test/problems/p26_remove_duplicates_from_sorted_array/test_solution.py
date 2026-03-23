import pytest

from problems.p26_remove_duplicates_from_sorted_array.solution import Solution


@pytest.mark.parametrize(
    argnames=["input_list", "expected_output_list"],
    argvalues=[
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4])
    ],
    ids=[
        "empty",
        "1 element non-repeating",
        "2 elements non-repeating",
        "3 elements, repeating",
        "n elements, repeating"
    ]
)
def test_solution(input_list: list[int], expected_output_list: list[int]):
    # for a, b in zip(input_list, expected_output_list):
    #     output = list(set(input_list))
    #     assert output == expected_output_list
    sol = Solution()
    output_len = sol.removeDuplicates(input_list)
    assert input_list[:output_len] == expected_output_list
