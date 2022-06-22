import sympy
import numpy
import matplotlib.pyplot as plt

analytic_solution = False
numerical_value_set = 0
values = [[1, 2, 4, 2 * numpy.pi], [1, 3, 4, 2 * numpy.pi]]
base = numpy.linspace(0, 10, 10000)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

if analytic_solution:
    z1 = sympy.Symbol('z1')
    z2 = sympy.Symbol('z2')
    z3 = sympy.Symbol('z3')
    k2 = sympy.Symbol('k2')

else:
    [z1, z2, z3, k2] = values[numerical_value_set]

l = sympy.Symbol('l')
r = sympy.Symbol('r')
tau = sympy.Symbol('tau')

M1 = sympy.Matrix([[-1, 1, 1, 0],
                   [1, z1/z2, - z1/z2, 0],
                   [0, sympy.exp(- 1j * k2 * l), sympy.exp(1j * k2 * l), -1],
                   [0, - sympy.exp(- 1j * k2 * l), sympy.exp(1j * k2 * l), z2/z3],
                   ])

'''M1 = sympy.Matrix([[-1, 1, 1, 0],
                   [1, z1/z2, - z1/z2, 0],
                   [0, sympy.cos(- k2 * l), sympy.cos(k2 * l), -1],
                   [0, sympy.cos(- k2 * l), sympy.cos(k2 * l), z2/z3],
                   ])'''

M3 = sympy.Matrix([[1], [1], [0], [0]])

M2 = (M1 ** -1) * M3

letters = ['r', 'a', 'b', 'tau']

print(M2[0].subs('l', base))

if not analytic_solution:
    sympy.plot(M2[0].subs(l, base), base)
    '''plt.plot(M2[0], (l, 0, 5))
    plt.legend()
    plt.show()'''
