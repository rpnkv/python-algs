import pytest

from easy.ex3105_longest_monothonic_subarray.solution import Solution


@pytest.mark.parametrize(
    argnames=["input_arr", "expected_output"],
    argvalues=[
        ([1, 4, 3, 3, 2], 2),
        ([3, 3, 3, 3], 1),
        ([3, 2, 1], 3),
        ([1, 1, 5], 2)
    ],
    ids=["base test 1", "base test 2", "base test 3", "test case 430"]
)
def test1(input_arr, expected_output):
    sol = Solution()
    assert sol.longestMonotonicSubarray(input_arr) == expected_output
