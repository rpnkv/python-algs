def count_distinct_elements(input_array: list[int]) -> int:
    count = 1

    if len(input_array) in [0, 1]:
        return len(input_array)

    # current = input_array[0]
    for i in range(1, len(input_array)):
        #   if input_array[i] != current:
        if input_array[i] != input_array[i - 1]:
            current = input_array[i]
            count += 1

    return count
