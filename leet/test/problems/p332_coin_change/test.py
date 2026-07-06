import pytest

cases = [
    pytest.param([2], 0, 0, id="my case 1"),
    pytest.param([2], 1, -1, id="my case 2"),
    pytest.param([2], 2, 1, id="my case 3"),
    pytest.param([1, 2], 0, 0, id="my case 1"),
    pytest.param([1, 2], 1, 1, id="my case 2"),
    pytest.param([1, 2], 2, 1, id="my case 2"),
    pytest.param([1, 2], 3, 2, id="my case 2"),
    pytest.param([1, 2], 4, 2, id="my case 2"),
    pytest.param([1, 2], 5, 3, id="my case 2"),
    pytest.param([1, 2, 5], 11, 3, id="example 1"),
    pytest.param([2], 3, -1, id="example 2"),
    pytest.param([1], 0, 0, id="example 3"),
    pytest.param([2], 1, -1, id="example 7"),
    pytest.param([1, 2, 5], 100, 20, id="case 16"),
    pytest.param([1, 2, 5], 11, 3, id="case 23"),
    pytest.param([186,419,83,408], 6249, 20, id="case 100"),
]


@pytest.mark.parametrize(["coins", "amount", "expected"], cases)
def test_recursive(coins, amount, expected):
    from problems.p332_coin_change.solution_recursive import Solution
    assert Solution().coinChange(coins, amount) == expected


@pytest.mark.parametrize(["coins", "amount", "expected"], cases)
def test_recursive_mem(coins, amount, expected):
    from problems.p332_coin_change.solution_recursive_mem import Solution
    assert Solution().coinChange(coins, amount) == expected


@pytest.mark.parametrize(["coins", "amount", "expected"], cases)
def test_recursive_mem_2(coins, amount, expected):
    from problems.p332_coin_change.solution_recursive_mem_2 import Solution
    assert Solution().coinChange(coins, amount) == expected


@pytest.mark.parametrize(["coins", "amount", "expected"], cases)
def test_bottom_up(coins, amount, expected):
    from problems.p332_coin_change.solution_bottom_up import Solution
    assert Solution().coinChange(coins, amount) == expected
