"""
The decimal number, 585 = 1001001001(2) (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

Thoughts:
- Due to the increased number of characters in base 10 palindroms are likely more rare
- Limiting to under one milion 6 chars is the max length of a palindrome
"""

double_pals = 0


def is_binary_pal(n):
    binary = str(bin(n)[2:])
    bin_pal = all([i == j for i, j in zip(binary, binary[::-1])])
    if bin_pal:
        print(n, binary)
        return True


for pal_length in range(1, 7):
    if pal_length % 2 == 0:  # Pal is even length need len // 2 chars
        len_unique_chars = 10 ** (pal_length // 2)
        for i in range(len_unique_chars // 10, len_unique_chars):
            pal_part = str(i)
            pal = int(pal_part + pal_part[::-1])
            if is_binary_pal(pal):
                double_pals += pal
    else:
        len_unique_chars = 10 ** (pal_length // 2)
        for i in range(10):
            for j in range(len_unique_chars // 10, len_unique_chars):
                pal_part = str(j)
                if j != 0:
                    pal = int(pal_part + str(i) + pal_part[::-1])
                else:
                    pal = i
                if is_binary_pal(pal):
                    double_pals += pal

print(double_pals)
