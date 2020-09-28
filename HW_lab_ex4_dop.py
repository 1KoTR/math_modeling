strNum = input()

c = strNum.__len__()

for i in range(c):
    print(strNum[c - i - 1], end="")