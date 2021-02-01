import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def F(v, t):
    dvdt = (b - k * v) / m
    return dvdt

t = np.linspace(0, 1000, 100)
m = 1000
b = 100
k = 10
v_0 = 100

solve_Bi = odeint(F, v_0, t)

plt.plot(t, solve_Bi[:,0])

plt.show()