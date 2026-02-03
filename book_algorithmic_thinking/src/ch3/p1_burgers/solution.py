def solve_t_simplified(m: int, n: int, t: int) -> int:
    first: int
    second: int

    if t == 0:
        return 0

    if t >= m:
        first = solve_t_simplified(m, n, t - m)
    else:
        first = -1

    if t >= n:
        second = solve_t_simplified(m, n, t - n)
    else:
        second = -1

    if first == -1 and second == -1:
        return -1
    else:
        return max(first, second) + 1


def solve_t(m: int, n: int, t: int) -> int:
    optimal_solution = solve_t_simplified(m, n, t)
    if optimal_solution >= 0:
        return optimal_solution

    for t_cycle in range(t - 1, -1, -1):
        current_solution = solve_t_simplified(m, n, t_cycle)
        if current_solution >= 0:
            return t_cycle - t - 1

    raise NotImplemented
