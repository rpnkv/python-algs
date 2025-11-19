# Given an array of numbers a_1, a_2, ..., a_n .
#
# You need to find the longest monotonic subarray (either strictly increasing or strictly decreasing) and return
# the pair of indices marking its start and end.
#
# Examples:
#
# [2, 7, 5, 4, 4, 3] -> {1, 3}
# [1, 1] -> {1, 1} // or {0, 0}


def execute(input_arr: list[int]) -> (int, int):
    right = 1

    prev_relation: str = None

    current_len = 0

    longest_results = {}

    while right < len(input_arr):
        current_relation: str

        if input_arr[right] - input_arr[right - 1] < 0:
            current_relation = "decreasing"
        elif input_arr[right - 1] - input_arr[right] > 0:
            current_relation = "increasing"
        else:
            current_relation = "equals"

        if ((current_relation == prev_relation) or (prev_relation is None)) and (current_relation != "equals"):
            # state gets verified, increase subsequence length
            current_len += 1
        else:
            # state is not verified, persist previous subsequence and reset current_length
            longest_results[current_len] = (right - current_len - 1, right - 1)
            current_len = 1

        prev_relation = current_relation
        right += 1

    max_len = max(longest_results.keys())
    return longest_results[max_len]


def test1():
    input_arr = [2, 7, 5, 4, 4, 3]
    expected_output = (1, 3)

    assert execute(input_arr) == expected_output


def test2():
    input_arr = [1, 1]
    actual_output = execute(input_arr)
    assert (
            actual_output == (0, 0) or
            actual_output == (1, 1)
    )

