import pytest

from problems.medium.p128_longest_consecutive_sequence.solution import Solution


@pytest.mark.parametrize(
    argnames=["input_nums", "expected_output"],
    argvalues=[
        ([100, 4, 200, 1, 3, 2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([1,0,1,2], 3)
    ],
    ids=[
        "example 1",
        "example 2",
        "example 3",
    ]
)
def test(input_nums, expected_output):
    sol = Solution()
    assert sol.longestConsecutive(input_nums) == expected_output
