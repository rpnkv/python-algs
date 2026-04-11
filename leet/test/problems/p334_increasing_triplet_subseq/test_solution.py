import pytest

from problems.p334_increasing_triplet_subseq.solution import Solution

TEST_CASES = [
    pytest.param([1, 2, -1, -1, 4], True, id="my case"),
    pytest.param([1, 1, -2, 6], False, id="case 77"),
]

sol = Solution()


@pytest.mark.parametrize(["input", "expected_result"], TEST_CASES)
def test(input: list[int], expected_result: int):
    assert sol.increasingTriplet(input) == expected_result
