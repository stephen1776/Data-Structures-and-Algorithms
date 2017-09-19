# Uses python3
'''
Task. In this problem, you are given a set of bars of gold and your goal is to take as much gold as possible
into your bag. There is just one copy of each bar and for each bar you can either take it or not (hence
you cannot take a fraction of a bar).
Input Format. The first line of the input contains the capacity W of a knapsack and the number n of bars
of gold. The next line contains n integers w0,w1,...,w_(n-1) defining the weights of the bars of gold.

Output Format. Output the maximum weight of gold that fits into a knapsack of capacity W.
'''
import sys

def optimal_weight(W, w):
    n = len(w)
    v0 = [0] * (n + 1)
    value = []
    for i in range(W + 1):
        value.append(list(v0))

    # Use algorithm from slides and book
    for j in range(1, n + 1):
        val = w[j - 1]
        for x in range(1, W + 1):
            if val > x:
                value[x][j] = value[x][j - 1]
            else:
                value[x][j] = max(value[x][j - 1], value[x - val][j - 1] + val)

    return value[W][n]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
