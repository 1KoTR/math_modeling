import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------- Пространство для анимации ----------
fig, ax = plt.subplots()

# ---------- Анимирумые объекты ----------
anim_obj_1, = plt.plot([], [], '-', lw=3, color='b')
anim_obj_2, = plt.plot([], [], 'o', color='r')

# ---------- Параметры объектов ----------
N = 100 # Количество точек анимации.

x1 = []
y1 = []

# Параметры второго объекта.
x2 = np.linspace(0, 2*np.pi, N)
y2 = np.cos(x2)

# ---------- Параметры анимации ----------
n = [] # Массив для определения номера кадра.
ax.set_xlim(0, 2*np.pi) # Пределы изменения X.
ax.set_ylim(-1, 1) # Пределы изменения Y.

# ---------- Функция подстановки параметров ----------
def update(frame):
    x1.append(frame)
    y1.append(np.sin(frame))
    anim_obj_1.set_data(x1, y1)
    
    # Передача номера кадра объекту 2.
    n.append(frame)
    anim_obj_2.set_data(x2[len(n) - 1], y2[len(n) - 1])
    
    # Украшение.
    ax.set_title('Какой-нибудь параметр {}'.format(frame))
    
# ---------- Анимация ----------
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, N), interval=100)

# Сохранение gif.
ani.save('pic.gif')