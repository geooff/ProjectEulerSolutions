"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

num_list = [x for x in range(20, 1, -1)]

def test_answer(test_int):
    for i in num_list:
        if test_int % i != 0:
            return False
    return True

base_ans = 1
for i in num_list:
    base_ans *= i

min_ans = base_ans
for i in num_list:
    print("Starting to divide by {}".format(i))
    while test_answer(min_ans):
        print(min_ans)
        if min_ans % i == 0:
            last_ans = int(min_ans)
            min_ans /= i
            if not test_answer(min_ans):
                min_ans = int(last_ans)
                break