def copy_list(l: list[int]) -> list[int]:
    copied = [0] * len(l)
    p_input = 0

    while p_input < len(l):
        copied[p_input] = l[p_input]
        p_input += 1

    return copied
