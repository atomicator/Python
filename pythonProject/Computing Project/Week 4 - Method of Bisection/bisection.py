import math


error = 1e-4
initial_range = [0, 10]
N = 3


def iterate_sqrt(n, maximum=initial_range[1], minimum=initial_range[0]):
    finished = False
    while not finished:
        mid = (maximum + minimum) / 2
        if mid ** 2 < n:
            minimum = mid
        else:
            maximum = mid

        if abs(mid ** 2 - n) < 1e-4:
            finished = True
    print(mid)
    return mid


def compare_results(n):
    guess = iterate_sqrt(n)
    actual = math.sqrt(n)
    difference = guess - actual
    return difference


for N in range(11)[1:]:
    print(compare_results(N))
