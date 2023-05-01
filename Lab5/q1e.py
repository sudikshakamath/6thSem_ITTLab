def sum_n(n):
    if(n <= 1):
        return n
    else:
        return n+sum_n(n-1)


n = int(input("Enter a number: "))
print(sum_n(n))
