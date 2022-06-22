import sympy

m1, m2, u1, u2, v1, v2 = sympy.symbols("m1 m2 u1 u2 v1 v2")

ke = m1 * u1 ** 2 + m2 * u2 ** 2 - m1 * v1 ** 2 - m2 - v2 ** 2

ke = ke.subs(v1, (m1 * u1 + m2 * u2 - m2 * v2) / m1)

print(ke)
sol = sympy.solve((ke, 0), (v2,))
print(sol)
