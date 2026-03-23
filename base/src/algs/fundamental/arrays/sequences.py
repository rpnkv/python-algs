def check_if_all_elements_are_equal(collection: list[int]) -> bool:
    for i in range(1, len(collection)):
        if collection[i] != collection[i - 1]:
            return False

    return True
