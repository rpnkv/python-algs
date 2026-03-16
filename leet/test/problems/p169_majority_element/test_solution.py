import pytest

from problems.p169_majority_element.naive_solution import Solution as NaiveSolution
from problems.p169_majority_element.expected_solution import Solution as ExpectedSolution


@pytest.mark.parametrize(
    argnames=["input_list", "expected_value"],
    argvalues=[
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2)
    ]
)
def test_naive_solution(input_list: list[int], expected_value: int):
    sol = NaiveSolution()
    assert sol.majorityElement(input_list) == expected_value


@pytest.mark.parametrize(
    argnames=["input_list", "expected_value"],
    argvalues=[
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2)
    ]
)
def test_naive_solution(input_list: list[int], expected_value: int):
    sol = ExpectedSolution()
    assert sol.majorityElement(input_list) == expected_value