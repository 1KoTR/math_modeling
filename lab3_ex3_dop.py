import numpy as np

l = int(input("Введите длину масива: "))
h = int(input("Введите ширину масива: "))
array1 = np.zeros((h, l))

array2 = np.zeros((l, h))
for (i, j), x in np.ndenumerate(array1):
    num = int(input(f"[{i}, {j}] = "))
    array1[(i, j)] = num
    array2[(j, i)] = num
    
array3 = np.zeros(l)
for i, x in np.ndenumerate(array3):
    array3[i] = array2[i].max() 
    
print("\narray1:\n", array1, 
      "\n\narray2:\n", array2, 
      "\n\narray3:\n", array3)