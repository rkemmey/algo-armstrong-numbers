# How can you make this more scalable and reusable later?
# an N-digit number that is equal to the sum of the Nth powers of its digits
''' convert to string for length. take power of each and sum.
test if equals, then add to list
'''
import math

def find_armstrong_numbers(numbers):
    arm_list = []

    for n in numbers:
        new_sum = 0
        str_n = str(n)
        power = len(str_n)
        for s in str_n:
            new_sum += math.pow(int(s), power)
        if new_sum == n:
            arm_list.append(n)
    return arm_list