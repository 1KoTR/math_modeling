import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_obj_1, = plt.plot([], [], '-', lw=3, color='b')
anim_obj_2, = plt.plot([], [], '-', lw=3, color='r')

N = 100
R = 1
R2 = 5

x1 = []
y1 = []

x2 = []
y2 = []

ax.set_xlim(-10, 10)
ax.set_ylim(-5, 5)

def update(frame):
    x1.append(R*(frame - np.sin(frame)))
    y1.append(R*(1 - np.cos(frame)))
    anim_obj_1.set_data(x1, y1)
    
    x2.append(R2*np.cos(frame)**3)
    y2.append(R2*np.sin(frame)**3)
    anim_obj_2.set_data(x2, y2)
    
ani = FuncAnimation(fig, update, frames=np.linspace(-10, 10, N))
ani.save('piq3c123.gif', fps=30)