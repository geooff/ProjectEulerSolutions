"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def is_pythag(a, b, c):
    if a**2 + b**2 == c**2:
        return True


def test():
    assert is_pythag(3,4,5)


def main():
    for i in range(1, 1001):
        for j in range(i+1, 1001):
            for k in range(j+1, 1001):
                if i+j+k == 1000:
                    if is_pythag(i,j,k):
                        print(i*j*k)
                        quit()


test()
main()