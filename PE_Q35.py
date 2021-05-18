"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, 
are themselves prime.

There are thirteen such primes below 100: 
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""


def eratosthenes(n):
    """Yields the sequence of prime numbers via the Sieve of Eratosthenes."""
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2  # first integer to test for primality
    primes = []
    while q <= n:
        p = D.pop(q, None)
        if p:
            x = p + q
            while x in D:
                x += p
            D[x] = p
        else:
            D[q * q] = q
            primes.append(q)
        q += 1
    return primes


primes = eratosthenes(1000000)

i = 0
circular_primes = 0
while primes:
    v = str(primes[i])
    local_primes = []
    for j in range(len(v)):
        if (lookup := int(v[j:] + v[:j])) not in primes:
            primes.pop(i)
            break

        local_primes.append(lookup)

        if len(local_primes) == len(v):
            local_primes = set(local_primes)
            circular_primes += len(local_primes)
            for k in local_primes:
                primes.remove(k)

print(circular_primes)
