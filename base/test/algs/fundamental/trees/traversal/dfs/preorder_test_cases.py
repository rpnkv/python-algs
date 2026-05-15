import pytest

TEST_CASES = [
    pytest.param([], [], id="0 nodes"),
    pytest.param([1], [1], id="1 node"),
    pytest.param([1, 2, None], [2, 1], id="2 nodes L"),
    pytest.param([1, None, 2], [1, 2], id="2 nodes R"),
    pytest.param([1, 2, 3], [2, 1, 3], id="3 nodes balanced"),
    pytest.param([1] + [2, None] + [3] + [None] * 3, [3, 2, 1], id="3 nodes unbalanced"),
]
