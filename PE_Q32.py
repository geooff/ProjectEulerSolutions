"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, 
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

# ex: 39 × 186 = 7254
from itertools import permutations
from typing import List


def list_to_int(values: List) -> int:
    return int("".join(map(str, values)))


perms = list(permutations(range(1, 10)))  # [:10000]
valid_perms = []

for i in perms:
    for j in range(len(i) - 1):
        a_len = len(i[: j + 1])
        a = list_to_int(i[: j + 1])
        if a_len > len(i) // 2:
            break
        for k in range(len(i[j:]) - 2):
            b = list_to_int(i[j + 1 : j + k + 2])
            c = list_to_int(i[j + k + 2 :])
            if a * b == c:
                if c not in valid_perms:
                    valid_perms.append(c)
            elif a * b > c:
                break

print(sum(valid_perms))
