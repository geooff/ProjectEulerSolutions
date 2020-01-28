"""
Question:
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
from math import floor

start_pal = 1000000
start_int = 999
stop_int = 100

def is_palindrome(test_int: int) -> bool:
    int_list = list(str(test_int))
    int_len = len(str(test_int))
    for i in range(floor(int_len/2)):
        if int_list[i] != int_list[int_len-i-1]:
            return False
    print("Found palindrome {}".format(test_int))
    return True


def is_three_digit(test_int: int) -> bool:
    if len(str(test_int)) == 3:
        return True


for i in range(start_pal, 10000, -1):
    if is_palindrome(i):
        for j in range(start_int, stop_int, -1):
            k = i / j
            if k == round(k) and is_three_digit(round(k)):
                print(j, k)
                quit()