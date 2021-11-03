# https://projecteuler.net/problem=7

"""
Using primesieve
"""
from utils.timings import timing
import pyprimesieve


@timing
def sol():
    print(pyprimesieve.primes_nth(10001))


if __name__ == '__main__':
    sol()
