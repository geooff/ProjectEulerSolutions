"""
The square root of 2 can be written as an infinite continued fraction.

...

The infinite continued fraction can be written, ,  indicates that 2 repeats ad infinitum. In a similar way, .

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for .

...
 
Hence the sequence of the first ten convergents for  are:

 ...

What is most surprising is that the important mathematical constant,

The first ten terms in the sequence of convergents for e are:

...

The sum of digits in the numerator of the 10th convergent is .

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for .
"""

# Note: Using python floats with ~16 decimal point precision isnt precise enough

from fractions import Fraction
import math
from decimal import Decimal, getcontext

getcontext().prec = 64


def eval_continued_feaction(series: list) -> int:
    val = 0
    series.reverse()
    for idx, j in enumerate(series):

        if idx == len(series) - 1:
            print(val + j)
            return Fraction(Decimal(val) + Decimal(j))

        val = Decimal(1) / (Decimal(j) + Decimal(val))
        print(val)


def make_e_series(len: int):
    k = 1
    series = [2]
    steps = math.ceil((len - 1) / 3)

    for i in range(steps):
        series = series + [1, k * 2, 1]
        k += 1

    return series[:len]


def get_sum_of_e_approx(ith):
    series = make_e_series(ith)
    print(series)
    fraction = eval_continued_feaction(series).limit_denominator(10 ** 62)
    print(fraction)

    numerator = fraction.numerator
    return sum([int(x) for x in str(numerator)])


print(get_sum_of_e_approx(100))
