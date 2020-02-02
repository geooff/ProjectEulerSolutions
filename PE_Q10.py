"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from math import ceil


def is_prime(test_int):
    if test_int == 2: return True
    for i in range(2, ceil(test_int**0.5)+1):
        if test_int % i == 0:
            return False
    return True


def test():
    assert is_prime(7)
    assert not is_prime(6)
    assert is_prime(5)
    assert not is_prime(4)
    assert is_prime(3)
    assert is_prime(2)


def main():
    prime_list = []
    for i in range(2, 2000000):
        if is_prime(i):
            prime_list.append(i)
    print(sum(prime_list))


test()
main()