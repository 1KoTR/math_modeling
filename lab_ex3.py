import matplotlib.pyplot as plt
import numpy as np

def circle(R = 1, title = "Circle"):
    x = np.arange(-R - 1, R + 1, 0.1)
    y = np.arange(-R - 1, R + 1, 0.1)
    X, Y = np.meshgrid(x, y)
    
    expr = X**2 + Y**2
    
    plt.contour(X, Y, expr, levels=[R**2])
    
    plt.axis("equal")
    plt.show()
    
def ellipse(a = 1, b = 1, title = "Ellipse"):
    x = np.arange(-a - 1, a + 1, 0.1)
    y = np.arange(-b - 1, b + 1, 0.1)
    X, Y = np.meshgrid(x, y)
    
    expr = (X/a)**2 + (Y/b)**2
    
    plt.contour(X, Y, expr, levels=[1])
    
    plt.axis("equal")
    plt.show()
    
circle(1)
ellipse(10, 5)