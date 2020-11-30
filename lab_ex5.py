import matplotlib.pyplot as plt
import numpy as np

def Spiral_painter(name = "Spiral", k = 1):
    fi = np.arange(0.01, 8*np.pi, 0.001)
    
    if (name == 1):
        expr = np.e**(k*fi)
    elif (name == 2):
        expr = k*fi
    elif (name == 3):
        expr = k/np.sqrt(fi)
    elif (name == 4):
        k = 3
        expr = np.sin(k*fi)
    
    x = expr*np.cos(fi)
    y = expr*np.sin(fi)
    
    plt.plot(x, y, label = "graph")
    
    plt.title(name)
    plt.legend()
    plt.axis("equal")
    
    plt.show()

print("1 - Логарифмическая спираль", "2 - Архимедова спираль", "3 - Жезл", "4 - Роза", sep='\n')
num = int(input("Введите номер одной из спиралей: "))

Spiral_painter(num)