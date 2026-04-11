import pytest

TEST_CASES = [
    pytest.param(["01:15", "02:00"], ["02:00", "03:00"], True, id="example 1"),
    pytest.param(["01:00", "02:00"], ["01:20", "03:00"], True, id="example 2"),
    pytest.param(["10:00", "11:00"], ["14:00", "15:00"], False, id="example 3"),

    pytest.param(["10:00", "11:00"], ["10:00", "15:00"], True, id="overlap by start"),
]


@pytest.mark.parametrize(["event1", "event2", "expected_output"], TEST_CASES)
def test_solution(event1: list[str], event2: list[str], expected_output: bool):
    from problems.p2446_determine_if_two_events_have_conflict.solution import Solution
    sol = Solution()
    assert sol.haveConflict(event1, event2) == expected_output
