# https://projecteuler.net/problem=1

# Upper bounding the problem statement = The smallest prime factor of a composite number N is less than or equal to
# square root of N. So the easiest way to solve this would be get get the square root of N.
import math
from itertools import islice, count

import pyprimesieve


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(math.sqrt(n) - 1)))


def hack_sol():
    max = 600851475143*600851475
    # max = 13195
    while max > 2:
        while max % 2 == 0:
            max = max/2
        while max % 5 == 0:
            max = max/5
        while max % 2 == 0:
            max = max/2
        for prime in pyprimesieve.primes(int(math.sqrt(max))):
            if max%prime == 0:
                max = int(max/prime)
                print(is_prime(max), max, prime)
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
    # hack_sol()
    sol()