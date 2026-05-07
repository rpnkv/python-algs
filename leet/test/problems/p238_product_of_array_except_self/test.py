import pytest

from problems.p238_product_of_array_except_self.solution import Solution

TEST_CASES = [
    pytest.param([1, 2, 3, 4], [24, 12, 8, 6], id="Example 1"),
    pytest.param([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0], id="Example 2"),
]

@pytest.mark.parametrize(["income", "expected_outcome"], TEST_CASES)
def test(income: list[int], expected_outcome: list[int]):
    assert Solution().productExceptSelf(income) == expected_outcome