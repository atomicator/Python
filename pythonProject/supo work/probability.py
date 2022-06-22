from math import factorial, e

limit = 20000

p = 0
n = 0
q = 0.99
l = 60

while n <= limit:
    p += (1 - (q ** n)) * (( l ** n) / factorial(n)) * (e ** (-1 * l))
    n += 1
    print(n)

print(p)
