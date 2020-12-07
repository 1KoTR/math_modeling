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

ax.set_xlim(0, L + L/10) # Пределы изменения X.
ax.set_ylim(0, H + H/10) # Пределы изменения Y.

# ----- Украшения -----
ax.set_xlabel(f'Дальность (max: {np.around(L, 3)}), м')
ax.set_ylabel(f'Высота (max: {np.around(H, 3)}), м')

ax.legend()

# ---------- Анимирумые объекты ----------
objLine, = plt.plot([], [], '--', lw=1, color='k', label='trajectory') # Траетория полёта шара.
objBall, = plt.plot([], [], '.', color='r', ms=20, label='ball') # Шар.

# ---------- Функция подстановки параметров ----------
xLine, yLine = [], []
def update(t):
    xLine.append(V_0*np.cos(alpha)*t) # Рассчитывает X
    yLine.append(V_0*np.sin(alpha)*t - (g*t**2)/2) # Рассчитывает Y
    
    objLine.set_data(xLine, yLine)

    objBall.set_data(xLine[::-1][0], yLine[::-1][0])

    # ----- Украшения -----
    ax.set_title(f'Время: {np.around(t, 3)} c' + \
                 f'\nРасстояние от начала: {np.around(xLine[::-1][0], 3)} м' + \
                 f'\nВысота от начала: {np.around(yLine[::-1][0], 3)} м')

# ----- Украшения -----
ax.set_xlabel(f'Дальность (max: {np.around(L, 3)}), м')
ax.set_ylabel(f'Высота (max: {np.around(H, 3)}), м')
ax.legend()
ax.grid()

# ---------- Вывод ----------
print(f'\nВремя полёта шара: {np.around(T, 3)} с')
print(f'Максимальная высота подъёма шара: {np.around(H, 3)} м')
print(f'Дальность полёта шара: {np.around(L, 3)} м')

t = np.linspace(0, T, 100)
anim = FuncAnimation(fig, update, t)
try:
    anim.save(f'trajectory[{outAlpha},{V_0}].gif', writer='pillow', fps=30) # Сохранение gif файла в папке с программой
except:
    print('Ошибка! Не удалось сохранить gif файл.')