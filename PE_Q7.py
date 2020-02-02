"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
from math import ceil


def is_prime(test_int):
    for i in range(ceil(test_int/2), 1, -1):
        if test_int % i == 0:
            return False
    return True


def full_list(test_list):
    if len(test_list) >= 10001:
        return True


def test():
    assert is_prime(7)


test()
prime_nums = []
count = 2
while not full_list(prime_nums):
    if is_prime(count):
        prime_nums.append(count)
    count += 1

print(prime_nums[-1])