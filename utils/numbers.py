import math


def get_factors(num):
    """
    Get factors for num > 2
    :param num:
    :return:
    """
    factors = []
    while num>1:
        for factor in range(2, num+1):
            while num%factor == 0:
                factors.append(factor)
                num = num/factor
    return factors


def is_perfect_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2