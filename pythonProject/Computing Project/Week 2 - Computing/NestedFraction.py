# NestedFraction.py
def nested_fraction(previous_nest):  # calculates the value of the nested fraction given the value of the previous one
    value = 1 + 1/(previous_nest)
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


n = 20
initial_value = 1
values = [initial_value]  # used to store the values, and already containing the first
digits = 10

value = initial_value
for i in range(n - 1):  # iterates to find the other values and add them to values
    value = nested_fraction(value)
    values.append(value)

print(values)

for num in values:  # This loop adjusts the length of each digit in values then prints them
    num = adjust_digits(num, digits)
    print(num)
