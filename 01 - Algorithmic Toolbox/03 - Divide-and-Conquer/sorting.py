# Uses python3
'''
Task. To force the given implementation of the quick sort algorithm to efficiently process sequences with
few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new
partition procedure should partition the array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.

Input Format. The first line of the input contains an integer 𝑛. The next line contains a sequence of 𝑛
integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.

Output Format. Output this sequence sorted in non-decreasing order.
'''
import sys
import random

#Max time used: 0.76/11.00, max memory used: 29732864/536870912.
def randomized_quick_sort(a):
    if len(a) < 2:
        return a
    red = [x for x in a[1:] if x < a[0]]
    white = [x for x in a if x == a[0]]
    blue = [x for x in a[1:] if x > a[0]]
    return randomized_quick_sort(red) + white + randomized_quick_sort(blue)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a = randomized_quick_sort(a)
    for x in a:
        print(x, end=' ')

#  Failed case #14/23: time limit exceeded (Time used: 21.98/11.00, memory used: 29179904/536870912.)
# def partition3(a, l, r):
#     #write your code here
#     #To handle equal elements, we replace the line
#     # m ← Partition(A, ℓ, r )
#     # with the line
#     # (m1,m2) ← Partition3(A, ℓ, r )
#     # such that
#     # for all ℓ ≤ k ≤ m1 − 1, A[k] < x
#     # for all m1 ≤ k ≤ m2, A[k] = x
#     # for all m2 + 1 ≤ k ≤ r , A[k] > x
#     x = a[l]
#     j = l  # count the lower bound
#     k = 0  # upper bound is j + k
#     for i in range(l + 1, r + 1):
#         # Add elements to the first partition following partition2
#         if a[i] < x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#         if k > 0:  # Remove an elements from the middle partition
#             k -= 1
#         # Add elements to the middle partition
#         if a[i] == x:
#             k += 1
#             a[i], a[j + k] = a[j + k], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j, j + k
#
#
# def partition2(a, l, r):
#     x = a[l]
#     j = l;
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j
#
#
# def randomized_quick_sort(a, l, r):
#     if l >= r:
#         return
#     k = random.randint(l, r)
#     a[l], a[k] = a[k], a[l]
#     #use partition3
#     #m = partition2(a, l, r)
#     #randomized_quick_sort(a, l, m - 1);
#     #randomized_quick_sort(a, m + 1, r);
#     m1, m2 = partition3(a, l, r)
#     randomized_quick_sort(a, l, m1 - 1);
#     randomized_quick_sort(a, m2 + 1, r);
#
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     randomized_quick_sort(a, 0, n - 1)
#     for x in a:
#         print(x, end=' ')
