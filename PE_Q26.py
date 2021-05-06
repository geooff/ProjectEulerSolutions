"""
A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from decimal import getcontext, Decimal

# Increase this number till your max repeating length doesnt change
decimal_depth = 5000
getcontext().prec = decimal_depth


def find_lrf(x):
    for i in range(2, len(x) // 2):
        seqs = [x[k : k + i] for k in range(0, len(x), i)][:-1]
        if seqs.count(seqs[0]) == len(seqs):
            return i
    return 0


repeating_lengths = []
for i in range(1, 1001):
    fraction = str(Decimal(1) / Decimal(i))[2:]
    repeating_lengths.append((i, find_lrf(fraction)))

repeating_lengths.sort(key=lambda x: x[1])
print(repeating_lengths)