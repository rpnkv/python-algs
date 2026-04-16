import pytest

from algs.fundamental.search.binary_search import search as search_while


def test_empty():
    assert search_while([], 0) == -1


@pytest.mark.parametrize(
    argnames=["arr", "target", "index"],
    argvalues=[
        ([1], 0, -1),
        ([1], 1, 0),
        ([1], 2, -1)
    ],
    #ids=["existing", "non-existing"]
)
def test_single(arr: list, target: int, index: int):
    assert search_while(arr, target) == index


@pytest.mark.parametrize(
    argnames=["arr", "target", "index"],
    argvalues=[
        # ([1, 2], 1, 0),
        # ([1, 2], 2, 1),
        # ([1, 2], 3, -1),
        ([0, 1], -1, -1),
        ([0, 1], 0, 0),
        ([0, 1], 1, 1),
        ([0, 1], 2, -1)
    ],
    #ids=["existing 1", "existing 2", "non-existing"]
)
def test_two(arr: list, target: int, index: int):
    assert search_while(arr, target) == index


@pytest.mark.parametrize(
    argnames=["arr", "target", "index"],
    argvalues=[
        ([1, 2, 3], 1, 0),
        ([1, 2, 3], 2, 1),
        ([1, 2, 3], 3, 2),
        ([1, 2, 3], 4, -1)
    ],
    ids=["existing 1", "existing 2", "existing 3", "non-existing"]
)
def test_three(arr: list, target: int, index: int):
    assert search_while(arr, target) == index


@pytest.mark.parametrize(
    argnames=["arr", "target", "index"],
    argvalues=[
        ([1, 2, 3, 4], 1, 0),
        ([1, 2, 3, 4], 2, 1),
        ([1, 2, 3, 4], 3, 2),
        ([1, 2, 3, 4], 4, 3),
        ([1, 2, 3, 4], 5, -1)
    ],
    ids=["existing 1", "existing 2", "existing 3", "existing 4", "non-existing"]
)
def test_four(arr: list, target: int, index: int):
    assert search_while(arr, target) == index


@pytest.mark.parametrize(
    argnames=["arr", "target", "index"],
    argvalues=[
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 2, 1),
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 4, 3),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 6, -1)
    ],
    ids=["existing 1", "existing 2", "existing 3", "existing 4", "existing 5", "non-existing"]
)
def test_five(arr: list, target: int, index: int):
    assert search_while(arr, target) == index


@pytest.mark.parametrize(
    argnames=["arr", "target", "index"],
    argvalues=[
        ([1, 2, 3, 4, 5, 6], 1, 0),
        ([1, 2, 3, 4, 5, 6], 2, 1),
        ([1, 2, 3, 4, 5, 6], 3, 2),
        ([1, 2, 3, 4, 5, 6], 4, 3),
        ([1, 2, 3, 4, 5, 6], 5, 4),
        ([1, 2, 3, 4, 5, 6], 6, 5),
        ([1, 2, 3, 4, 5, 6], 7, -1)
    ],
    ids=["existing 1", "existing 2", "existing 3", "existing 4", "existing 5", "existing 6", "non-existing"]
)
def test_six(arr: list, target: int, index: int):
    assert search_while(arr, target) == index
