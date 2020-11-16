from sympy import symbols, Abs
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities

x, y, z = symbols("x y z")

expr = Abs(x - 5) - 3 # Выражение с модулем.

sol = reduce_abs_inequality(expr, '<', x) # Находит множество решений. 
print(sol)

print()

expr = y + 2 > 0 # Выражение с без модуля.

sol = reduce_rational_inequalities([[expr]], y) # Находит множество решений. 
print(sol)

print()

expr = x**2 <= 0
 
sol = reduce_rational_inequalities([[expr]], x) # Находит множество решений. 
print(sol)