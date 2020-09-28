b1 = int(input())
q = int(input())
n = int(input())
for i in range(1, n + 1, 1):
    b = b1 * q**(i-1)
    print(b, end = " ")