import pytest


def test_base():
    from problems.easy.p283_move_zeores_to_end.move_zeores_to_end_ds import Solution
    sol = Solution()
    input_list = [0, 1, 0, 3, 12]
    expected_output_list = [1, 3, 12, 0, 0]

    sol.moveZeroesInv(input_list)

    assert input_list == expected_output_list


@pytest.mark.parametrize(
    argnames=["input_list", "expected_output_list"],
    argvalues=[
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([1], [1]),
        ([1,2,3,4],[1,2,3,4])
    ],
    ids=["lc0", "single el", "no zeroes"]
)
def test_my(input_list: list[int], expected_output_list: list[int]):
    from problems.easy.p283_move_zeores_to_end.move_zeroes_to_end import Solution
    sol = Solution()

    sol.moveZeroes(input_list)

    assert input_list == expected_output_list
