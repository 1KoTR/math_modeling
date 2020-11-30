import matplotlib.pyplot as plt
import numpy as np

def Lissajous_curve(a = 1, A = 1, b = 1, B = 1):
    t = np.arange(0, 10*np.pi, 0.01)
    
    x = A*np.sin(a*t + np.pi/2)
    y = B*np.sin(b*t)
    
    plt.plot(x, y, color = 'r')
    plt.axis("equal")
    
    plt.show()

Lissajous_curve(a = 5, A = 5, b = 8, B = 3)