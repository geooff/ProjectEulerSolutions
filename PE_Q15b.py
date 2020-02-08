"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
from math import factorial as fact


def bin_permutations(n):
    """
    Calculate the permutations of binary elements. We don't calculate them directly as it isn't fast enough, instead
    we use the following formula
    https://en.wikipedia.org/wiki/Binomial_coefficient"""
    return int((fact(2*n))/(fact(n))**2)


print(bin_permutations(20))