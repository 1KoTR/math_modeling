a = 5
b = 4
if (a == 5) and (b == 5):
    print("a and b == 5")
elif (a == 5) or (b == 5):
    print("a or b == 5")
else:
    print("a and b != 5")

if (a != 6) or ((a == 5) and (b != 5)):
    print("a != 6 or (a == 5 and b != 5)")