"""
By replacing the 1st digit of the 2-digit number *3, 
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, 
being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, 
by replacing part of the number (not necessarily adjacent digits) with the same digit, 
is part of an eight prime value family.
"""

# ex: 56xx3 --> Yeilds 7 combos

from math import log10


def eratosthenes():
    """Yields the sequence of prime numbers via the Sieve of Eratosthenes."""
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2  # first integer to test for primality
    while True:
        p = D.pop(q, None)
        if p:
            x = p + q
            while x in D:
                x += p
            D[x] = p
        else:
            D[q * q] = q
            yield q
        q += 1


# Note, two chars window didn't work. Trying for three char
def find_mates_three(primes):
    max_base = int(log10(max(primes)))
    counts = {}
    for i in range(max_base - 1):
        for j in range(i + 1, max_base):
            for k in range(j + 1, max_base):
                for p in primes:
                    l = list(str(p))
                    if len(l) < max_base:
                        l = (max_base - len(l)) * ["_"] + l
                    x, y, z = l[i], l[j], l[k]
                    if x == y == z and x != "_":
                        l[i] = l[j] = l[k] = "x"
                        p = "".join(l)
                        counts[p] = counts.get(p, 0) + 1
    return [k for k, v in counts.items() if v >= 8]


primes = []
for n in eratosthenes():

    primes.append(n)

    # Search first million primes
    if n > 1000000:
        values = find_mates_three(primes)
        break

for pattern in values:
    for i in range(10):
        prime_candidate = int(pattern.replace("x", str(i)))
        if prime_candidate in primes:
            print(prime_candidate)
            quit()
