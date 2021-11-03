# https://projecteuler.net/problem=5

"""
Naive. Reduce all number to prime multipliers.
1x2x3x4x5x6x7x8x9x10
1x2x3x(2x2)x5x(3x2)x7x(2x2x2)x(3x3)x(2x5)
1x2x3x2x5x7x2x3

The idea is to check if the next number's factors are already accounted for. If yes.
"""
import math
from functools import reduce
from itertools import islice, count

import pyprimesieve
from timeit import timeit

from utils.lists import list_difference
from utils.numbers import get_factors
from utils.timings import timing


@timing
def hack_sol():
    max = 1000
    current_factors = [2, 3]
    for i in range(4, max+1):
        delta = list_difference(get_factors(i), current_factors)
        if len(delta) == 0:
            pass
        else:
            current_factors += delta
    print(current_factors)
    print(reduce(lambda x, y: x * y, current_factors, 1))


if __name__ == '__main__':
    # for i in range(20):
    #     print(i, get_factors(i))

    hack_sol()
