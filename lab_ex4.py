def Func(a, b):
    y_N = []
    for i in range(a + 1, b):
        y_N.append(i**2)
    return y_N
    
a = int(input("a = "))
b = int(input("b = "))
print(Func(a, b))