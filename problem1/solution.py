"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

from itertools import combinations
from functools import reduce
from time import monotonic
import operator


def loop_based(factors, maximum):
    """ Loops over the integer range and sums numbers divisible by any factor. 
    
    The operating time is linearly proportional to both the number of factors, and to the maximum value. """
    total = 0
    for val in range(maximum):
        if any((evenly_divisible(val, factor) for factor in factors)):
            total += val
    return total


def set_based(factors, maximum):
    """ Finds the solution by using the inclusion-exclusion principle. This solution is only guaranteed to work
    if the factors are all pair-wise coprime. 
    
    The operating time is exponential with respect to the number of factors. This is because the number of 
    k-Combinations for all k is 2**n where n is the number of factors.
    """
    total = 0
    for i in range(1, len(factors) + 1):
        for n in combinations(factors, i):
            n = reduce(operator.mul, n)
            total += ((-1) ** (i + 1)) * n * integer_summation((maximum - 1) // n)
    return total


def evenly_divisible(numerator, denominator):
    return numerator % denominator == 0


def integer_summation(n):
    return int((n * (n + 1) / 2))


def main():
    factors = (3, 5)
    maximum = 1000
    t0 = monotonic()
    loop_sum = loop_based(factors, maximum)
    t1 = monotonic()
    set_sum = set_based(factors, maximum)
    t2 = monotonic()

    assert loop_sum == set_sum
    print(f"The sum was {set_sum}")
    print(f"Loop based took {t1 - t0} seconds.\nSet based took {t2 - t1} seconds.\nLoop Time/Set Time = {(t1-t0)/(t2-t1)}")


if __name__ == "__main__":
    main()
