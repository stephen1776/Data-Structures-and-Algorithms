# Uses python3
# Problem Description
# Task. Given two integers 𝑎 and 𝑏, find their least common multiple.
# Input Format. The two integers 𝑎 and 𝑏 are given in the same line separated by space.
# Constraints. 1 ≤ 𝑎, 𝑏 ≤ 2 · 109.
# Output Format. Output the least common multiple of 𝑎 and 𝑏.
import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a * b // gcd(a, b) # use integer floor division


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#
#     return a*b
#
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     a, b = map(int, input.split())
#     print(lcm_naive(a, b))

