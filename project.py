import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# ---------- Пространство для анимации ----------
fig, ax = plt.subplots()

# ---------- Анимирумые объекты ----------
objLine, = plt.plot([], [], '--', lw=2, color='k') # Траетория полёта шара.
objBall, = plt.plot([], [], 'o', color='r') # Шар.

xLine, yLine = [], []
xBall, yBall = [], []
def update(frame):
    xLine = V_0*np.cos(alpha)*frame
    yLine = V_0*np.sin(alpha)*frame - (g*frame**2)/2
    
    objLine.set_data(xLine, yLine)
    
    
# ---------- Ввод данных пользователем ----------
try:
    g = float(input('Введите ускорение свободного падения [0; +oo)\ng = '))
except:
    print('Ошибка! Неверное значение.\nDefault: g = 9.8')
    g = 9.8
    
try:
    alpha = float(input('Введите угол [-90; 90]\nalpha = '))
    if not(-90 <= alpha <= 90):
        print('Ошибка! Неверное значение.\nDefault: alpha = 0')
        alpha = 0
except:
    print('Ошибка! Неверное значение.\nDefault: alpha = 0')
    alpha = 0
    
try:
    V_0 = float(input('Введите начальную скорость [0; +oo)\nV_0 = '))
except:
    print('Ошибка! Неверное значение.\nDefault: V_0 = 0')
    V_0 = 0

# ---------- Рассчёт данных ----------
T = (2*V_0*np.sin(alpha))/g # Время полёта шара.
L = (V_0**2*np.sin(2*alpha)) # Расстояние на которое пролетел шар.
H = (V_0**2*np.sin(alpha)**2)/(2*g) # Высота подъёма шара.
print(T, L, H)

# ---------- График ----------


# ---------- Вывод ----------
frames = np.linspace(0, int(H + 1), 100)
anim = FuncAnimation(fig, update, frames)
anim.save('trajectory.gif', fps=30)