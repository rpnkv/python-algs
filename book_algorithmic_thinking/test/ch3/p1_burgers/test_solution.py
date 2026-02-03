import pytest

from ch3.p1_burgers.solution import solve_t
from ch3.p1_burgers.solution import solve_t_simplified

ARG_NAMES = ["m", "n", "t", "expected_answer"]

ARG_VALUES = [
    (4, 9, 22, 3),
    (4, 9, 54, 11),
    (4, 9, 15, -3),
]


@pytest.mark.parametrize(
    argnames=ARG_NAMES,
    argvalues=[(case[0], case[1], case[2], -1 if case[3] < 0 else case[3]) for case in ARG_VALUES]
)
def test_solution_simplified(m: int, n: int, t: int, expected_answer: int):
    assert solve_t_simplified(m, n, t) == expected_answer


@pytest.mark.parametrize(
    argnames=ARG_NAMES,
    argvalues=ARG_VALUES
)
def test_solution(m: int, n: int, t: int, expected_answer: int):
    assert solve_t(m, n, t) == expected_answer
