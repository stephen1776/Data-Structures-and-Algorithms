# Uses python3
# Problem Description
# Task. Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).
# Input Format. The input consists of a single integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 107.
# Output Format. Output the last digit of 𝐹𝑛.
import sys
def fibonacci_last_digit(n):
    a, b = 0, 1
    for i in range(n):
        #if 0 <= n & n <= 107:
        a, b = b % 10, (a + b) % 10
        # else:
        #     print("out of range")
    return a


if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(fibonacci_last_digit(n))


# Starter Code
# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % 10