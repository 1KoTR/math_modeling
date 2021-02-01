import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def F(m, t):
    dmdt = k * m
    return dmdt

t = np.linspace(0, 5, 100)
m_0 = 1
k = 1

solve_Bi = odeint(F, m_0, t)

plt.plot(t, solve_Bi[:,0])

plt.show()