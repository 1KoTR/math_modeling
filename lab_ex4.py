import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину
x = np.arange(-5, 5, 0.01)

# Определяем функцию для системы диф. уравнений
def diff_func(tmp, x): # z - изменяемая величина для системы
    y, w = tmp # Указание изменяемых функций, через z
	
    # Первое уравнение системы
    dy_dt = w
    # Второе уравнение системы
    dw_dt = -4 * w - 5 * y
    
    return dy_dt, dw_dt

# Определяем начальные значения и параметры,
# входящие в систему диф. уравнений
y0 = 4
dy0_dt = -1

# Начальное значение изменяемой величины системы
tmp0 = y0, dy0_dt

# Решаем систему диф. уравнений
sol = odeint(diff_func, tmp0, x)

# Строим решение в виде графика
plt.plot(x, sol[:, 1], 'b')
plt.plot(sol[:, 1], sol[:, 0], 'g')
plt.plot(sol[:, 0], sol[:, 1], 'r')
plt.show()