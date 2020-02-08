"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
"""
0000000000000000000011111111111111111111
0000000000000000000101111111111111111111
0000000000000000001001111111111111111111
...
1000000000000000000001111111111111111111
1000000000000000000010111111111111111111
...
1100000000000000000000111111111111111111
...
...
1111111111111111111100000000000000000000

Every time a 1 moves to the left all the ones to the right of it move back to right most spots
"""

start = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
         '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']


def done(input_list):
    """Are all the 1's left of all the 0's?"""
    return '1' not in "".join(input_list).lstrip('1')


def clumpted_ones(input_list):
    """Does the right most 1 have another 1 to its left? Ex. 1010110"""
    return "".join(input_list).rstrip('0')[-2:] == '11'


def boost_highest(input_list):
    output = input_list
    observed_one = False
    for idx, ele in reversed(list(enumerate(input_list))):
        if ele == '1':
            observed_one = True
        if ele == '0' and observed_one:
            output[idx] = '1'
            output[idx+1] = '0'
            rem = output[idx+1:]
            output[idx+1:] = ['0']*rem.count('0') + ['1']*rem.count('1')
            break
    return output


def boost(input_list):
    output = input_list
    for idx, ele in reversed(list(enumerate(input_list))):
        if ele == '1':
            output[idx] = '0'
            output[idx - 1] = '1'
            break
    return output


def test():
    assert start.count('0') == 20
    assert start.count('1') == 20
    assert done(['1', '1', '1', '0', '0', '0'])
    assert not done(['1', '0', '1', '0', '1', '0'])
    assert boost_highest(['0', '1', '1', '0', '0']) == ['1', '0', '0', '0', '1']
    assert boost_highest(['1', '0', '1', '1', '0']) == ['1', '1', '0', '0', '1']
    assert clumpted_ones(['1', '0', '1', '1', '0'])
    assert clumpted_ones(['1', '0', '1', '1', '1'])
    assert not clumpted_ones(['1', '1', '0', '1', '0'])
    assert boost(['1', '0', '0', '1']) == ['1', '0', '1', '0']


def main(input_list):
    paths = 1
    while not done(input_list):
        # print("".join(input_list))
        if clumpted_ones(input_list):
            input_list = boost_highest(input_list)
        else:
            input_list = boost(input_list)
        paths += 1
    # print("".join(input_list))
    print(paths)


test()
main(start)

# This method was too slow. See solution PE_15b.py
