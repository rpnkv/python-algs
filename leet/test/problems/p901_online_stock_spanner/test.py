import pytest

from problems.p901_online_stock_spanner.bruteforce_solution import StockSpanner

TEST_CASES = [
    pytest.param(
        [100, 80, 60, 70, 60, 75, 85],
        [1, 1, 1, 2, 1, 4, 6], id="Example 1")
]


@pytest.mark.parametrize(["prices", "expected_span"], TEST_CASES)
def test_bruteforce(prices: list[int], expected_span: list[int]):
    ss = StockSpanner()

    for price, expected_span in zip(prices, expected_span):
        actual_span = ss.next(price)
        assert actual_span == expected_span