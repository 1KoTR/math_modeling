N = int(input("N = "))

i = 2
while (i < N):
    if (N % i == 0):
        print(i)
        N /= i
    else:
        i += 1
print(int(N))