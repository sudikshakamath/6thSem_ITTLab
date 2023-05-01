m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))


for i in range(m, n+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
