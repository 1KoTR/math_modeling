import matplotlib.pyplot as plt # Импорт модуля.

x = [1, 2, 3]
y = [6, 8, 4]

# color - цвет графика (линии).
# label - назване графика.
# marker - маркер графика (точки на концах).
# ms - размерность маркера (точек).
plt.plot(x, y, color='b', label="line", marker='.', ms=20)

plt.xlabel("Coord: x") # Подпись абциссы.
plt.ylabel("Coord: y") # Подпись ординаты.
plt.title("Base") # Подпись всего графика.
plt.axis("equal") # Делает оси равными.
plt.legend() # Вызов окна подписей графиков (label)
plt.grid() # отображение координатной сетки.

plt.show() # Выводит график.