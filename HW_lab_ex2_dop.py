a = int(input())
b = int(input())
c = int(input())

if (a < b + c) and (b < a + c) and (c < a + b):
    print("Треуг. сущ.")
    if (a == b == c):
        print("Рав/с. треуг.")
    elif (a == b) or (b == c) or (c == a):
        print("Рав/б. треуг.")
    elif (a**2 == b**2 + c**2) or (b**2 == c**2 + a**2) or (c**2 == b**2 + a**2):
        print("Прям. треуг.")
    else:
        print("Раз/с. треуг.")
else:
    print("Треуг. не сущ.")