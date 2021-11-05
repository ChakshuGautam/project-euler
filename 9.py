# https://projecteuler.net/problem=9
"""
Loop over 1000 three times to get all triplets
"""
import math

from utils.numbers import is_perfect_square
from utils.timings import timing


@timing
def brute_force_sol():
    found = False
    s = 1000
    upper_bound_a = int((s - 3) / 3)
    while not found:
        for a in range(1, upper_bound_a):
            for b in range(a, int((s - a) / 2)):
                square_c = a * a + b * b
                if is_perfect_square(square_c) and (a + b + math.isqrt(square_c)) == s:
                    print("New", a, b, math.sqrt(a * a + b * b), a * b * math.isqrt(square_c))
                    found = True
                    break
            if found:
                break


@timing
def sol():
    # TODO: Use the m, n representation and simplify
    pass


if __name__ == '__main__':
    sol()
