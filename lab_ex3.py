from sympy import symbols, solveset, Eq, sin

x = symbols('x')

expr = x**2 + x + 1/x + 1/x**2

print(f"x = {solveset(Eq(expr, 4), x)}")

E = symbols('E')
e = 0.8
M = 9

expr = E - e*sin(E) - M

print(f"E = {solveset(expr, E)}")