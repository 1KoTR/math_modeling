def MyFunc(a, b):
    x = 3*a - 2**b
    y = 2*b + 3**a
    return x, y # Возвращает два знаяения в виде кортежа.

result = MyFunc(2, 3)
print(result)
print(result[0], result[1])
print(type(result))