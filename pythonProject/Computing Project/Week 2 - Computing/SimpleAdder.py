# SimpleAdder.py

# A script that adds two numbers

kwh = float(input("Enter the power in kilowatt hours per day:\n"))  # The bumber to be converted

watts = (kwh / 24) * 1000  # converts the number

print(f"{kwh} kWh / day is equivalent to {watts} W.\n")  # prints the result
