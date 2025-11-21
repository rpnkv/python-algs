import timeit

from common import bench_utils
from problems.hard.p23.input_generator import produce_full
from problems.hard.p23.p23_merge_k_sorted_lists_heapq import Solution

test_input = produce_full(
    # elements_per_list=int(math.pow(10,4))
    elements_per_list=int(1)
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
