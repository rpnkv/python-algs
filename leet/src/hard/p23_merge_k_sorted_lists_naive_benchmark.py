import timeit

from bench.timeit_sketches import utils
from hard.input_generator import produce_full
from hard.p23_merge_k_sorted_lists_naive import Solution

test_input = produce_full(
    #elements_per_list=int(math.pow(10,4))
)

sol = Solution()

stmt = lambda: sol.mergeKLists(test_input)

number = 100
results = timeit.repeat(
    stmt=stmt,
    number=number,
    repeat=5
)

utils.verbose_results(results, number)
