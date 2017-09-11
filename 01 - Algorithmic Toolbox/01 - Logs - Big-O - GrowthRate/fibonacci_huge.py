# Uses python3
# Problem Description
# Task. Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).
# Input Format. The input consists of two integers 𝑛 and 𝑚 given on the same line (separated by a space).
# Constraints. 1 ≤ 𝑛 ≤ 1018, 2 ≤ 𝑚 ≤ 105.
# Output Format. Output 𝐹𝑛 mod 𝑚.
# exit cntrl+d
import sys

def fib(n, m):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a % m

def fibonacci_huge(n,m):
    if n <= 1:
        return n

    a = 1
    b = 1
    pisano_period = 1

    while (a, b) != (0, 1):
        a, b = b, (a + b) % m
        pisano_period += 1
    return fib(n % pisano_period, m)

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibonacci_huge(n, m))


# Starter Code
# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % m
#
# if __name__ == '__main__':
#     input = sys.stdin.read();
#     n, m = map(int, input.split())
#     print(get_fibonacci_huge_naive(n, m))
