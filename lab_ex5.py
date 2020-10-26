def S_figure(num = 0):
    S = 0
    if (num == 1):
        h = int(input("h = "))
        b = int(input("b = "))
        S = h*b/2
    elif (num == 2):
        a = int(input("a = "))
        b = int(input("b = "))
        S = a*b
    elif (num == 3):
        r = int(input("r = "))
        S = 3.14*r**2
    else:
        print("\nТакой фигуры нет в списке!")
    return S

number = int(input("\t- Треугольник (1)\n\t- Прямоугольник (2)\n\t- Круг (3)\n\nВыберите номер фигуры: "))
S = S_figure(number)
print("Площадь фигуры:", S)