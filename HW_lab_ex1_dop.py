a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

dis = b**2 - 4*a*c
if (dis < 0):
    print("Нет действительных корней.")
else:
    x1 = (-b + dis**(0.5)) / (2*a)
    x2 = (-b - dis**(0.5)) / (2*a)
    if (dis == 0):
        print("Один корень. X =", x1)
    else:
        print("Два корня. \n\tX1 =", x1, "\n\tX2 =", x2)