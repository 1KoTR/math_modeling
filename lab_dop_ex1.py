from sympy.vector import CoordSys3D
from math import acos, degrees

def v_angle(v_1, v_2):
    res = (v_1.dot(v_2))/(v_1.magnitude()*v_2.magnitude())
    return degrees(acos(res.evalf()))

N = CoordSys3D('N')

a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k
c = -5*N.i - 6*N.j + 12*N.k

print(v_angle(a, b))
print(v_angle(a, c))
print(v_angle(b, c))