import pytest

from problems.p14_longest_common_prefix.solution import Solution
from problems.p14_longest_common_prefix.solution_arch import SolutionArch

TEST_CASES = [
    pytest.param(["flower", "flow", "flight"], "fl", id="Example 1"),
    pytest.param(["dog", "racecar", "car"], "", id="Example 2"),
]


@pytest.mark.parametrize(["incoming_strings", "expected_outcome"], TEST_CASES)
def test_not_optimal(incoming_strings: list[str], expected_outcome: str):
    assert SolutionArch.longest_common_prefix_not_optimal(incoming_strings) == expected_outcome


@pytest.mark.parametrize(["incoming_strings", "expected_outcome"], TEST_CASES)
def test_optimal(incoming_strings: list[str], expected_outcome: str):
    assert SolutionArch.longest_common_prefix_optimal(incoming_strings) == expected_outcome


@pytest.mark.parametrize(["incoming_strings", "expected_outcome"], TEST_CASES)
def test_super_optimal(incoming_strings: list[str], expected_outcome: str):
    assert SolutionArch.longest_common_prefix_super_optimal(incoming_strings) == expected_outcome


@pytest.mark.parametrize(["incoming_strings", "expected_outcome"], TEST_CASES)
def test_newest(incoming_strings: list[str], expected_outcome: str):
    assert Solution().longestCommonPrefix(incoming_strings) == expected_outcome
