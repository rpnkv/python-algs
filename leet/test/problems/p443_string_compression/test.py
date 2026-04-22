import pytest

from problems.p443_string_compression.solution import Solution

TEST_CASES = [
    pytest.param(["a", "a", "b", "b", "c", "c", "c"], 6, id="Example 1"),
    pytest.param(["a"], 1, id="Example 2"),
    pytest.param(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], 4, id="Example 3"),
]

@pytest.mark.parametrize(["input_string_list", "expected_output_string_length"], TEST_CASES)
def test(input_string_list: list[str], expected_output_string_length: str):
    assert Solution().compress(input_string_list) == expected_output_string_length
