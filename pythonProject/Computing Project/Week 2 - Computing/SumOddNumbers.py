# SumOddNumbers.py

# This sums the values of the first N odd numbers (N is given by the user) and checks that it equals the expected value
# of N ** 2

N = input("How many odd numbers should be summed?\n")
valid = True

try:
    N = int(N)
except ValueError:
    print("Please enter a number")
    valid = False

if N < 0:
    print("The number cannot be negative")
    valid = False

if valid:
    total = 0
    i = 1
    while i <= N:
        total += (2 * i - 1)
        i += 1
    print(f"The sum of the first {N} odd integers is {total}")

    if total == N ** 2:
        print(f"The total, {total}, is equal to {N} squared, as expected")
    else:
        print(f"The total, {total}, does not equal {N} squared")
