# "a = 0" и "b = 1" задаются стандартное значение.
# Без этого будет ошибка!
# def MyFunc(a, b):
#   return 3*a - 2**b
def MyFunc(a = 0, b = 1):
    return 3*a - 2**b

print(MyFunc())