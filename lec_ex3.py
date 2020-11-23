import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(R = 1, title = "Circle plotter"):
    x = np.arange(-20, 20, 0.1)
    y = np.arange(-20, 20, 0.1)
    X, Y = np.meshgrid(x, y) # Указание на неявное задание координат.
    
    f_xy = X**2 + Y**2 # Уравнение кривой.
    
    plt.contour(X, Y, f_xy, levels=[R**2]) # Команда рисование для неявнозаданных кривых
    
    plt.axis("equal")
    plt.show() # Выводит график.
    
circle_plotter(3)