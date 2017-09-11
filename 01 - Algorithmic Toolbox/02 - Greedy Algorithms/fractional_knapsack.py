# Uses python3
# Problem: Maximizing the Value of a Loot
# Problem Description
# Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
# Input Format. The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
# The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the
# value and the weight of 𝑖-th item, respectively.
# Constraints. 1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑊 ≤ 2 · 106; 0 ≤ 𝑣𝑖 ≤ 2 · 106, 0 < 𝑤𝑖 ≤ 2 · 106 for all 1 ≤ 𝑖 ≤ 𝑛. All the
# numbers are integers.
# Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute
# value of the difference between the answer of your program and the optimal value should be at most
# 10−3. To ensure this, output your answer with at least four digits after the decimal point (otherwise
# your answer, while being computed correctly, can turn out to be wrong because of rounding issues).
import sys

def get_optimal_value(capacity, weights, values):
    max_value = 0
    list_A = list(zip(values, weights))
    list_A.sort(key=lambda item: item[0] / item[1], reverse=True)
    values = [item[0] for item in list_A]
    weights = [item[1] for item in list_A]

    for value, weight in zip(values, weights):
        if capacity == 0:
            return max_value
        min_weight = min(weight, capacity)
        max_value += min_weight * (value / weight)
        weight -= min_weight
        capacity -= min_weight

    return max_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
