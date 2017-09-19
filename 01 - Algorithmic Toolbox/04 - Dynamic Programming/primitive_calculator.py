# Uses python3
'''
Task. Given an integer n, compute the minimum number of operations needed to obtain the number n
starting from the number 1.

Input Format. The input consists of a single integer 1 <= n <= 10^6.

Output Format. In the first line, output the minimum number k of operations needed to get n from 1.
In the second line output a sequence of intermediate numbers. That is, the second line should contain
positive integers a0, a2, ... , ak=1 such that a0 = 1, a_(k-1) = n and for all 0 <= i < k - 1, a_(i+1) is equal to
either ai + 1, 2ai, or 3ai. If there are many such sequences, output any one of them.
'''
import sys

def optimal_sequence(n):
    sequence = []

    v = [0]*(n+1)
    for i in range(1, n+1):
        v[i] = v[i-1] + 1;
        if i % 2 == 0:
            v[i] = min(v[i//2]+1, v[i])
        if i % 3 == 0:
            v[i] = min(v[i//3]+1, v[i])

    while n >= 1:
        sequence.append(n)
        if n % 3 == 0 and v[n//3] == v[n] - 1:
            n = n // 3
        elif n % 2 == 0 and v[n//2] == v[n] - 1:
            n = n // 2
        else:
            n = n - 1

    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')