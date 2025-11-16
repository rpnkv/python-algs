import timeit

from bench.timeit_sketches import utils

number = 100
results = timeit.repeat(
    # stmt=lambda: time.sleep(0.001),
    stmt="time.sleep(sleep_time)",
    # stmt=lambda: time.sleep(globals()["sleep_time"]),
    setup="time.sleep(0.005); sleep_time:float=0.002",
    # setup=lambda : time.sleep(0.01),
    number=number,
    # globals=globals(),
    repeat=6
)

utils.verbose_results(results, number)
