import pytest

TEST_CASES = [
    pytest.param([], [], id="Empty"),
    pytest.param([2], [2], id="1 node"),
    pytest.param([1, 2, None], [1, 2, None], id="2 nodes left"),
    pytest.param([1, None, 2], [1, None, 2], id="2 nodes right"),
    pytest.param([1, 2, 3], [1, 2, 3], id="3 nodes balanced"),
    pytest.param([1, 2, None, 3, None, None, None], [1, 2, None, 3] + [None] * 3, id="3 nodes unbalanced"),
]
