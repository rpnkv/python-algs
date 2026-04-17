import pytest

from problems.p901_online_stock_spanner.bruteforce_solution import StockSpanner as bruteforece_solution
from problems.p901_online_stock_spanner.expected_solution import StockSpanner as expected_solution

TEST_CASES = [
    pytest.param([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6], id="Example 1"),
    pytest.param([10, 15, 20, 20], [1, 2, 3, 4], id="My case 1: continuous"),
    pytest.param([10, 15, 20, 20, 15], [1, 2, 3, 4, 1], id="My case 2: breaking"),
]


@pytest.mark.parametrize(["prices", "expected_span"], TEST_CASES)
def test_bruteforce(prices: list[int], expected_span: list[int]):
    ss = bruteforece_solution()

    for price, expected_span in zip(prices, expected_span):
        actual_span = ss.next(price)
        assert actual_span == expected_span


@pytest.mark.parametrize(["prices", "expected_span"], TEST_CASES)
def test_expected(prices: list[int], expected_span: list[int]):
    ss = expected_solution()

    for price, expected_span in zip(prices, expected_span):
        actual_span = ss.next(price)
        assert actual_span == expected_span


