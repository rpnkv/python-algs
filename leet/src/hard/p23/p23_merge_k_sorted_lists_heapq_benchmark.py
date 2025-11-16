import math
import timeit

from bench.timeit_sketches import utils
from hard.p23.input_generator import produce_full
from hard.p23.p23_merge_k_sorted_lists_heapq import Solution

test_input = produce_full(
    #elements_per_list=int(math.pow(10,4))
    elements_per_list=int(1)
)

assert (len(test_input)) == math.pow(10,4)

for head in test_input:
    assert head.next is None

sol = Solution()

stmt = lambda: sol.mergeKLists(test_input)

number = 100
results = timeit.repeat(
    stmt=stmt,
    number=number,
    repeat=5
)

utils.verbose_results(results, number)
