str = input("Enter the string to be checked:")
flag = 0
for i in range(0, int(len(str)/2)):
    if str[i] != str[len(str)-i-1]:
        flag=1
        break
if flag == 1:
    print("Not a palindrome")
else:
    print("Palidrome")