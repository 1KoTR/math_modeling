import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# ---------- Ввод данных ----------
# ----- Ускорение свободного падения -----
try:
    g = float(input('Введите ускорение свободного падения (0; +oo)\ng = '))
    if (g < 0):
        print('Ошибка! Значение не входит в заданный диапазон.\nDefault: g = 9.8')
        g = 9.8
except:
    print('Ошибка! Неверное значение.\nDefault: g = 9.8')
    g = 9.8

# ----- Угол -----
try:
    alpha = float(input('\nВведите угол (0; 90)\nalpha = '))
    if not(0 < alpha < 90):
        print('Ошибка! Значение не входит в заданный диапазон.\nDefault: alpha = 45')
        alpha = 45
except:
    print('Ошибка! Неверное значение.\nDefault: alpha = 45')
    alpha = 45
    
# ----- Начальна скорость -----
try:
    V_0 = float(input('\nВведите начальную скорость (0; +oo)\nV_0 = '))
    if (V_0 < 0):
        print('Ошибка! Значение не входит в заданный диапазон.\nDefault: V_0 = 10')
        V_0 = 10
except:
    print('Ошибка! Неверное значение.\nDefault: V_0 = 10')
    V_0 = 10

# ---------- Рассчёт данных ----------
outAlpha = alpha
alpha *= np.pi/180 # Перевод радиан в градусы

T = np.abs((2*V_0*np.sin(alpha))/g) # Время полёта шара.
L = V_0*np.cos(alpha)*T # Дальность полёта шар.
H = (V_0**2*np.sin(alpha)**2)/(2*g) # Высота подъёма шара.

# ---------- Пространство для анимации ----------
fig, ax = plt.subplots()

ax.set_xlim(0, max([L + L/10, H + H/10])) # Пределы изменения X.
ax.set_ylim(0, max([L + L/10, H + H/10])) # Пределы изменения Y.

# ---------- Анимирумые объекты ----------
objLine, = plt.plot([], [], '--', lw=1, color='k') # Траетория полёта шара.
objBall, = plt.plot([], [], '.', color='r', ms=25) # Шар.

objVector_X, = plt.plot([], [], '--', lw=2, color='r', marker='>', ms=5)
objVector_Y, = plt.plot([], [], '--', lw=2, color='r', ms=5)

# ---------- Функция подстановки параметров ----------
xLine, yLine = [], []
def Update(t):
    X = V_0*np.cos(alpha)*t # Рассчитывает X
    Y = V_0*np.sin(alpha)*t - (g*t**2)/2 # Рассчитывает Y
    
    xLine.append(X)
    yLine.append(Y)
    objLine.set_data(xLine, yLine)

    objBall.set_data(xLine[::-1][0], yLine[::-1][0])
    
    X_2 = X + V_0*np.cos(alpha)*max([H, L])/(5*V_0)
    objVector_X.set_data([X, X_2], Y)
    
    Y_2 = Y + (V_0*np.sin(alpha) - g*t)*max([H, L])/(5*V_0)
    objVector_Y.set_marker('^' if (Y_2 > Y) else 'v')
    objVector_Y.set_data(X, [Y, Y_2])

    # ----- Украшения -----
    ax.set_title(f'Время: {np.around(t, 3)} c' + \
                 f'\nРасстояние от начала: {np.around(xLine[::-1][0], 3)} м' + \
                 f'\nВысота от начала: {np.around(yLine[::-1][0], 3)} м')

# ----- Украшения -----
ax.set_xlabel(f'Расстояние (max: {np.around(L, 3)}), м')
ax.set_ylabel(f'Высота (max: {np.around(H, 3)}), м')
ax.set_aspect('equal', adjustable='box') # Делает график квадратным.
ax.grid() # Создаёт сетку на графике

# ---------- Вывод ----------
print(f'\nВремя полёта шара: {np.around(T, 3)} с')
print(f'Высота подъёма шара: {np.around(H, 3)} м')
print(f'Дальность полёта шара: {np.around(L, 3)} м')

t = np.linspace(0, T, 60)
anim = FuncAnimation(fig, Update, t)
try:
    anim.save(f'trajectory[{outAlpha},{V_0}].gif', writer='pillow', fps=50) # Сохранение gif файла в папке с программой
except:
    print('Ошибка! Не удалось сохранить gif файл.')