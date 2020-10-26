def E_mech(m = 0, h = 0, v = 0, g = 9.81):
    """ Высчитывает полную механическую энергию.
        На вход получает массу тела m,
        высоту h, на которой находится тело,
        скорость тела v.
    """
    E_p = m*g*h
    E_k = m*v**2/2
    
    return E_p + E_k

m = int(input("m = "))
h = int(input("h = "))
v = int(input("v = "))
print(E_mech(m, h, v))