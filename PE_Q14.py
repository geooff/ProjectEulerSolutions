"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def even_transform(input_int):
    return input_int/2


def odd_transform(input_int):
    return 3*input_int+1


def collatz(num):
    steps = 1
    while num != 1:
        if num % 2 == 0:
            num = even_transform(num)
        else:
            num = odd_transform(num)
        steps += 1
    return steps


def test():
    assert collatz(13) == 10


def main():
    max_len = 0
    for i in range(1, 1000001):
        length = collatz(i)
        if length > max_len:
            max_len = length
            print("New max collatz length for {} of {}".format(i, length))


test()
main()