# Uses python3
'''
Task. The goal in this code problem is to check whether an input sequence contains a majority element.

Input Format. The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative
integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.

Output Format. Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times,
and 0 otherwise.
'''
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    # First divide the Array into 2 halves, then recursively call on this.
    mid = (right - left) // 2
    left_m = get_majority_element(a, left, left + mid)
    right_m = get_majority_element(a, left + mid, right)
    left_count = 0

    # Now compare the numbers with the part of the array
    # that we are evaluating at this point (a[left:right)
    for i in range(left, right):
        if a[i] == left_m:
            left_count += 1
    if left_count > mid:
        return left_m

    # If the count adds up to more than the half of the array being
    # evaluated, then return that majority number
    right_count = 0
    for i in range(left, right):
        if a[i] == right_m:
            right_count += 1
    if right_count > mid:
        return right_m
    # return no majority element
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
