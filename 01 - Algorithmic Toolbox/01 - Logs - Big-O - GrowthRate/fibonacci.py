# Uses python3
# Compute a small fibonacci number
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    n = int(input())
    print(fib(n))

# Starter code
# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib(n - 1) + calc_fib(n - 2)
#
# n = int(input())
# print(calc_fib(n))
