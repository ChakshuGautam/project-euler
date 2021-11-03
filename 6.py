# https://projecteuler.net/problem=6

"""
(n(n+1)/2)^2 - (n(n+1)(2n+1)/6
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
def sol():
    n = 100
    diff = int((n*(n+1)/2)**2 - n*(n+1)*(2*n+1)/6)
    print(diff)


if __name__ == '__main__':
    sol()
