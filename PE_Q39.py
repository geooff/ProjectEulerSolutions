"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

Thoughts:
c**2 == b**2 + a**2
p = a + b + c
Lengths can only be ints
p // 3 < c < p - 2

More accuratly:
(a**2/3 + b**2/3)**3/2 < c < p - 2
"""

max_set = 0
for i in range(3,1001):
    uniq = set()
    c = i // 3 - 1
    while c <= i - 2:
        for b in range(1, c):
            a = i - c - b
            # print(c,b,a)
            if a < 0:
                break
            if c**2 - b**2 == a**2:
                uniq.add("".join(sorted([str(c),str(b),str(a)])))
        c += 1
    if len(uniq) > max_set:
        max_set = len(uniq)
        print(i, uniq)
        

        