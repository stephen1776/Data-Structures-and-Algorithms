# Uses python3
# Problem
#
# Given a sequence of non-negative integers a0,…,an−1, find the maximum pairwise product,
# that is, the largest integer that can be obtained by multiplying two different elements from the sequence
# (or, more formally, max0≤i≠j≤n−1aiaj). Different elements here mean ai and aj with i≠j
# (it can be the case that ai=aj).

# Input format
#
# The first line of the input contains an integer n. The next line contains n non-negative integers a0,…,an−1 (separated by spaces).
# Constraints
#
# 2≤n≤2⋅105; 0≤a0,…,an−1≤105.
# Output format
#
# Output a single number — the maximum pairwise product.

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)
max1 = max(a)
a.pop(a.index(max(a)))
max2 = max(a)
print(max1 * max2)







# starter Code
# n = int(input())
# a = [int(x) for x in input().split()]
# assert(len(a) == n)
#
# result = 0
#
# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]
#
# print(result)
