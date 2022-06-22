# SimpleAdder.py

# A script that adds two numbers

a = input("Enter the first number:\n")
b = input("Enter the second number:\n")

total = int(a) + int(b)

print(f"The sum of {a} and {b} is {total}.\n")

# Note: This program converts the input to integers. If floats are entered, int returns a value error. If a and b are
# strings (meaning the int commands are removed), then total will be a string made of the text in a followed by the
# text in b.
