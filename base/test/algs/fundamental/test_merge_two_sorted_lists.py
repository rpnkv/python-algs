from algs.fundamental.merge_two_sorted_lists import merge


def test_0():
    #l1, l2, expected_output
    l1 = [1, 3, 5]
    l2 = [2, 4, 6]

    expected_output = [1, 2, 3, 4, 5, 6]

    actual_output = merge(l1, l2)

    assert actual_output == expected_output
