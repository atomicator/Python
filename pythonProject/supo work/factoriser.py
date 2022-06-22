import sympy
a = sympy.symbols("a")
b = sympy.symbols("b")

e = a ** 2 - 4 * a * b + b ** 2

print(sympy.factor(e))
