"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

(21) 22 23 24 (25)
20  (7)  8  (9) 10
19  6  (1)  2 11
18  (5)  4  (3) 12
(17) 16 15 14 (13)

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
# 1, 3, 5, 7, 9, 13, 17, 21, 25
# Comments: For layer there are observations with an increasing offset from last layers max
# Offsets:
# n = 1 --> offset = 0
# n = 3 --> offset = 2 (3,5,7,9)
# n = 5 --> offset = 4 (13,17,21,25)

# ex. n=5_1, 9 + 4*1 = 13
# ex. n=5_2, 9 + 4*2 = 17
# ...

array = [1]
offset = 2
n = 500
for i in range(n):
    start = array[-1]
    for j in range(1, 5):
        array.append(start + offset * j)
    offset += 2

print(sum(array))