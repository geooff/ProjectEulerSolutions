"""
Euler discovered the remarkable quadratic formula:

y = n^2 + n + 41 

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. 
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, 
which produces 80 primes for the consecutive values 0 <= n <= 79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where abs(a) <= 1000 and abs(b) <= 1000

Find the product of the coefficients, a and b, 
for the quadratic expression that produces the maximum number of primes for consecutive values of n, 
starting with 0.
"""


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 6
    while f <= r:
        if n % (f - 1) == 0:
            return False
        if n % (f + 1) == 0:
            return False
        f += 6
    return True

sustained_streaks = []
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        n = 0
        while is_prime(n ** 2 + a * n + b):
            n += 1
            sustained_streaks.append((a, b, n))

sustained_streaks = sorted(sustained_streaks, key=lambda x: x[2])[-1]
print(sustained_streaks[0] * sustained_streaks[1])