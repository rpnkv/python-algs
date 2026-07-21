import pytest

CASES = [
    pytest.param([2, -3, 4, -2, 2, 1, -1, 4], 8, id="example 1N"),
    pytest.param([-1], -1, id="example 1N"),
]


@pytest.mark.parametrize(["inp", "exp"], CASES)
def test_bruteforce(inp, exp):
    from problems.p53_maximum_subarray.solution_bruteforce import Solution
    assert Solution().maxSubArray(inp) == exp


@pytest.mark.parametrize(["inp", "exp"], CASES)
def test_bruteforce(inp, exp):
    from problems.p53_maximum_subarray.solution_kadane import Solution
    assert Solution().maxSubArray(inp) == exp
