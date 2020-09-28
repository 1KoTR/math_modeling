a = float(input())
b = float(input())

if (b == 0):
    print("b == 0")
elif (a % b == 0):
    print("Д без ост.")
else:
    print("Ост. = ", a % b, sep = "")
    print("Ч = ", a / b, sep = "")