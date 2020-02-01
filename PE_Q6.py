"""
The sum of the squares of the first ten natural numbers is, 1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is, (1+2+...+10)^2=55^2=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def calc_sum_square(range_int):
    return_int = 0
    for i in range(1, range_int+1):
        return_int += i**2
    return return_int


def calc_square_sum(range_int):
    return_int = 0
    for i in range(1, range_int + 1):
        return_int += i
    return return_int ** 2


def test():
    assert calc_sum_square(10) == 385
    assert calc_square_sum(10) == 3025

test()

print(calc_square_sum(100) - calc_sum_square(100))