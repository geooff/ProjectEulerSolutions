"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable 
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. 

The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def get_sum_divisors(parent):
    output = []
    for x in range(1, parent):
        if parent % x == 0:
            output.append(x)
    return sum(output)

output = []
for x in range(1, 10001):
    print(f"Testing number: {x}")
    div_sum_1 = get_sum_divisors(x)
    div_sum_2 = get_sum_divisors(div_sum_1)
    if x == div_sum_2 and div_sum_1 != div_sum_2:
        print(f"Match found numbers: {x} and {div_sum_2}")
        output.append(x)

print(sum(output))