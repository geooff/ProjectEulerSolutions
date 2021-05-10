"""
In the United Kingdom the currency is made up of pound (£) and pence (p). 
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

# Brute Force Method
# combos = 0

# for two in range(2):
#     for one in range(3):
#         for fifty in range(5):
#             for twenty in range(11):
#                 for ten in range(21):
#                     for five in range(41):
#                         if (
#                             one * 1.0
#                             + fifty * 0.5
#                             + twenty * 0.2
#                             + ten * 0.1
#                             + five * 0.05
#                         ) > 2.0:
#                             break
#                         for twoc in range(101):
#                             if (
#                                 one * 1.0
#                                 + fifty * 0.5
#                                 + twenty * 0.2
#                                 + ten * 0.1
#                                 + five * 0.05
#                                 + twoc * 0.02
#                             ) > 2.0:
#                                 break
#                             for onec in range(201):

#                                 if (
#                                     two * 2.0
#                                     + one * 1.0
#                                     + fifty * 0.5
#                                     + twenty * 0.2
#                                     + ten * 0.1
#                                     + five * 0.05
#                                     + twoc * 0.02
#                                     + onec * 0.01
#                                 ) > 2.0:
#                                     break
#                                 elif (
#                                     two * 2.0
#                                     + one * 1.0
#                                     + fifty * 0.5
#                                     + twenty * 0.2
#                                     + ten * 0.1
#                                     + five * 0.05
#                                     + twoc * 0.02
#                                     + onec * 0.01
#                                     == 2.0
#                                 ):
#                                     combos += 1
# print(combos)

# Dynamic method
target = 200  # Our target value, 200p = £2
coins = [1, 2, 5, 10, 20, 50, 100, 200]  # Our 8 different coins represented as cents
ways = [1] + [0] * target  # Init our lookup table to be len(target) + 1

for coin in coins:
    # Start at value of coin (reason: £1 coin doesn't make a difference till we reach sum of £1)
    # end at target plus one
    for i in range(coin, target + 1):
        # Each value is based on lookback based on current coins value
        # This lookback value is added to the sum
        ways[i] += ways[i - coin]

print(ways[-1])