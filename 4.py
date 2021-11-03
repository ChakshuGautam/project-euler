# https://projecteuler.net/problem=4

"""
Naive. Get all the palendrome numbers from 100^2 to 999^2
Type 1: X1 X2 X3 X2 X1 => A total of 9*10*10 combinations
Type 2: X1 X2 X3 X3 X2 X1 => 900 for this as well.
1800 numbers to be tested for factors between 100-999
"""
import math
from itertools import islice, count

import pyprimesieve
from timeit import timeit

from utils.timings import timing


def reverse_num(num):
    return int(str(num)[::-1])


@timing
def hack_sol():
    current_count = 1000
    while current_count >= 100:
        current_count = current_count-1
        reverse_count = reverse_num(current_count)
        current_number = current_count*1000 + reverse_count
        found = False
        pair = None
        for i in range(999, 100, -1):
            x = current_number / i
            if int(x) > i:
                if current_number % i == 0 and x <= 999:
                    pair = (i, int(x))
                    found = True
                    break
        if found:
            print(current_number, pair)
            break


def sol():
    x = 600851475143
    divisor = 2
    while x != 1:
        if x % divisor == 0:
            x = x / divisor
            divisor -= 1
        divisor += 1
    print(divisor)


if __name__ == '__main__':
    # print(reverse_num(18))
    hack_sol()
    # sol()