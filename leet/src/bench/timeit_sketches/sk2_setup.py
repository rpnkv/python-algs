import time
import timeit

from bench.timeit_sketches import utils


class MyDataStructure:
    def __init__(self):
        self.init_counter = 0
        self.execute_counter = 0

    def initialize(self):
        time.sleep(0.003)
        self.init_counter += 1

    def execute(self):
        time.sleep(0.003)
        self.execute_counter += 1

    def __str__(self):
        return f"{self.init_counter}, {self.execute_counter}"

    def __repr__(self):
        return f"{self.init_counter}, {self.execute_counter}"


my_ds = MyDataStructure()

number = 100
results = timeit.repeat(
    stmt=my_ds.execute,
    setup=my_ds.initialize,
    number=number,
    #globals=globals(),
    repeat=5
)

utils.verbose_results(results, number)

print(my_ds)
