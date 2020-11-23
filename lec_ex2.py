import matplotlib.pyplot as plt
import numpy as np

def parabola_plotter(a = 1, b = 1, c = 0, title = "parabola plotter"):
    x = np.arange(-10, 10, 0.01)
    y = a*x**2 + b*x + c
    
    plt.plot(x, y, label="parabola") # Создает график с названием (parabola).
    plt.xlabel('Coord: X') # название горизонтальной оси.
    plt.ylabel('Coord: Y') # Название вертикальной оси.
    plt.title(title) # Название всего графика.
    plt.legend() # Вывод названия графика.
    
    plt.show() # Выводит график.
    
parabola_plotter()