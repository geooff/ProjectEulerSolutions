"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 
918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be 
formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

Thoughts:
Solution must have all digits 1-9 
10^8 < Solution < 10^9
"""

max_conprod = 0
i = 1
j = 1
con_prod = ""
while True:
    con_prod += str(i * j)
    j += 1

    # Numbers in solution repeating or 0's in there
    if "0" in con_prod or len(set(con_prod)) != len(con_prod):
        con_prod = ""
        i += 1
        j = 1

    #Each num 1-9 is in solution and each number not repeating
    if all([str(x) in con_prod for x in range(1, 10)]) and len(set(con_prod)) == len(con_prod): 
        max_conprod = int(con_prod)
        print(max_conprod, i)