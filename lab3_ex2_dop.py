import numpy as np

array1 = np.zeros(5)
for i, x in np.ndenumerate(array1):
    array1[i] = input(f"{i} = ")
    if (i == (3,)):
        break
print(array1)

index = int(input("Введите индекс: "))
number = int(input("Введите число: "))

array2 = np.insert(array1, index, number)
array2.resize(5)
print(array2)