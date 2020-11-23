from sympy.vector import CoordSys3D
from sympy import symbols, solveset

N = CoordSys3D('N')
x = symbols('x')

a = 7*N.i + 2*N.j - 8*N.k
b = -4*N.i + x*N.j + 9*N.k

cos_AB = (a.dot(b))/(a.magnitude()*b.magnitude())

print(solveset(cos_AB.evalf(), x))