import timeit

from bench.timeit_sketches import utils
from hard.p23.input_generator import produce_full
from hard.p23.p23_merge_k_sorted_lists_naive import Solution


def benchmark(test_input, number: int, repeat: int) -> list[float]:
    sol = Solution()

    stmt = lambda: sol.mergeKLists(test_input)

    return timeit.repeat(
        stmt=stmt,
        number=number,
        repeat=repeat
    )


if __name__ == "__main__":
    number = 1000
    repeat = 5
    import math
    results = benchmark(
        test_input=produce_full(
            #elements_per_list=int(4)
            elements_per_list=int(math.pow(10,4))
        ),
        number=number,
        repeat=repeat
    )

    #print(results)
    utils.verbose_results(results, number)
