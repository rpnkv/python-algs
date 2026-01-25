import pytest

from problems.easy.p83_remove_dupl_from_sorted_ll.solution import Solution

sol = Solution()


@pytest.mark.parametrize(
    argnames=["input", "expected_output"],
    argvalues=[
        ([1]), ([1]),
        ([1, 1]), ([1]),
        ([1, 1, 1]), ([1]),
        ([1, 1, 1, 2]), ([1, 2]),
        ([1, 2, 2]), ([1, 2]),
        ([1, 2, 2, 2]), ([1, 2]),
        ([1, 2, 3]), ([1, 2, 3]),
    ]
)
def test_solution(input_list, expected_output_list):
    assert sol.deleteDuplicates(input_list) == expected_output_list
