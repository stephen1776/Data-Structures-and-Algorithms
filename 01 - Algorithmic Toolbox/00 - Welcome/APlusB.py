# Uses python3
# There are two ways of running this program:
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 APlusB.py < dataset.txt
# Problem. Given two digits a and b, find a+b.
#
# Input format. The first line of the input contains two integers a and b (separated by a space).
#
# Constraints. 0≤a,b≤9.

# Output format. Output a+b.

import sys

def APlusB(a, b):
    if 0 <= a and b <= 9:
        return a + b
    else:
        return "Error"

if __name__ == '__main__':
    input = sys.stdin.read()
    tokens = input.split()
    a = int(tokens[0])
    b = int(tokens[1])
    print(a + b)


# import sys
#
# input = sys.stdin.read()
# tokens = input.split()
# a = int(tokens[0])
# b = int(tokens[1])
# print(a + b)