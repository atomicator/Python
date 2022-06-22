# SquareRootSequence.py

# This uses iterative methods to calculate the value of a square root sequence

import math


def nested_root(previous_root):  # calculates the value of the root using the value of the previous one
    value = math.sqrt(1 + previous_root)
    return value


def adjust_digits(number, length):  # adjusts the number of digits of a given float of integer (returning it as text)
    text = str(number)
    if len(text) <= length:
        if not ("." in text):
            text += "."
        text += "0" * (length - len(text))
    else:
        text = text[:length]
    return text


n = 20  # defining the constants
initial_value = 1
values = [initial_value]
digits = 10

value = initial_value
for i in range(n - 1):  # iterates and calculates the values
    value = nested_root(value)
    values.append(value)

print(values)

for num in values:
    num = adjust_digits(num, digits)
    print(num)

# This tends to a value of 1.61803398, the same as the expected value of (1 + root 5) / 2
