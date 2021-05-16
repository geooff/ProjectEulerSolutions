"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

Thoughts:
What is the upper limit, there must be one if we can make a sum?
Its likely easier to brute force then do any real math
"""
from math import factorial

curious_nums = 0
empty = 0
n = 10

while True:
    sum_facts = sum([factorial(int(i)) for i in str(n)])
    if sum_facts == n:
        print("Match!")
        curious_nums += n
        n += 1
        empty = 0
    else:
        empty += 1
        print(f"No match for last {empty}")
        n += 1
    print(curious_nums)