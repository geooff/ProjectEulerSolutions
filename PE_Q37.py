"""
The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Thoughts:
Its easy to make prime numbers (use eratosthenes)
"""


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


primes = []
truncatable_members = 0
truncatable_sum = 0

for n in eratosthenes():
    n = str(n)
    # print(n)
    primes.append(n)

    chars = len(n) - 1
    for i in range(1, len(n)):
        if n[i:] in primes and n[:-i] in primes:
            chars -= 1
        else:
            break

        if chars == 0:
            truncatable_members += 1
            truncatable_sum += int(n)
            print(f"{n} is a truncatable primes")

        if truncatable_members == 11:
            print(f"Found all 11 truncatable primes. They sum to {truncatable_sum}")
            quit()