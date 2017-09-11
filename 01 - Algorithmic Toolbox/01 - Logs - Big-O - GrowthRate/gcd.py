# Uses python3
# Problem Description
# Task. Given two integers 𝑎 and 𝑏, find their greatest common divisor.
# Input Format. The two integers 𝑎, 𝑏 are given in the same line separated by space.
# Constraints. 1 ≤ 𝑎, 𝑏 ≤ 2 · 109.
# Output Format. Output GCD(𝑎, 𝑏).
# Run python gcd.py then enter two numbers and press ctrl-d/ctrl-z
import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))


# Starter Code
# import sys
#
# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d
#
#     return current_gcd
#
# if __name__ == "__main__":
#     input = sys.stdin.read()
#     a, b = map(int, input.split())
#     print(gcd_naive(a, b))