from algs.fundamental.copy_list_manually import copy_list


def test():
    input = [2, 2, 3, 4, 5]

    output = copy_list(input)

    assert input == output
