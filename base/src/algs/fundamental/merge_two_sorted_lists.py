def merge(l1: list[int], l2: list[int]) -> list[int]:
    pos1 = pos2 = 0
    out = []

    while pos1 < len(l1) and pos2 < len(l2):
        if l1[pos1] < l2[pos2]:
            next_num = l1[pos1]
            pos1 += 1
        else:
            next_num = l2[pos2]
            pos2 += 1

        out.append(next_num)

    if pos1 == len(l1):
        out += l2[pos2:]

    if pos2 == len(l2):
        out += l1[pos1:]

    return out
