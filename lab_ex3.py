import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def F(v, t):
    dvdt = k * v**2 / m + a_0
    return dvdt

t = np.linspace(0, 25, 100)
m = 10
a_0 = 2
k = -0.05
v_0 = 0

solve_Bi = odeint(F, v_0, t)

plt.plot(t, solve_Bi[:,0])

plt.show()