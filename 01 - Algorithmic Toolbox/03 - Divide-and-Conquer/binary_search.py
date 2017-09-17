# Uses python3
'''
Task. The goal in this code problem is to implement the binary search algorithm.

Input Format. The first line of the input contains an integer 𝑛 and a sequence 𝑎0 < 𝑎1 < . . . < 𝑎𝑛−1 of
𝑛 pairwise distinct positive integers in increasing order.
The next line contains an integer 𝑘 and 𝑘 positive integers 𝑏0, 𝑏1, . . . , 𝑏𝑘−1.

Output Format. For all 𝑖 from 0 to 𝑘 − 1, output an index 0 ≤ 𝑗 ≤ 𝑛 − 1 such that 𝑎𝑗 = 𝑏𝑖 or −1 if there
is no such index.
'''
import sys, math

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    while left <= right:
        mid = math.floor(left + (right - left) // 2)
        if mid == len(a):
            return -1
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end=' ')
