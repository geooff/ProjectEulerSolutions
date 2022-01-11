"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101_1_12131415161718192021... = 1 cat 2 cat 3 cat ... cat 9 cat 10

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""

stop = 1000000
idx = 0
values = set([1, 10, 100, 1000, 10000, 100000, 1000000])
prod = 1
for i in range(1, stop):
    i = str(i)  # String-ify our int so we can index

    for j in range(len(i)):

        if idx + j + 1 in values:
            print("idx + j + 1 in values")
            prod *= int(i[j])
            print(prod)

    idx += len(i)

print(prod)
