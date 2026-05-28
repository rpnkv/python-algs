import pytest

from problems.p703_kth_largest_element_in_stream.solution import KthLargest

TEST_CASES = [
    pytest.param((3, [4, 5, 8, 2]), [3, 5, 10, 9, 4], [4, 5, 5, 8, 8], id="Example 1"),
    pytest.param((4, [7, 7, 7, 7, 8, 3]), [2, 10, 9, 9], [7, 7, 7, 8], id="Example 2"),
    pytest.param((1, []), [3,-2,5,10,9], [3,3,5,10,10], id="Example X"),
    # ["KthLargest", [1, []], "add", [3], "add", [-2], "add", [5], "add", [10], "add", [9]]
]


@pytest.mark.parametrize(["constructor_params", "incoming", "expected_outcome"], TEST_CASES)
def test(constructor_params: tuple[int, list[int]], incoming: list[int], expected_outcome: list[int]):
    s = KthLargest(constructor_params[0], constructor_params[1])

    for i, o in zip(incoming, expected_outcome):
        assert s.add(i) == o
