n = int(input("Enter number of elements in list: "))
list1 = []
for i in range(0, n):
    ele = input()
    list1.append(ele)
list2 = list(reversed(list1))
if(list2 == list1):
    print("it is a palindrome")
else:
    print("not a palindrome")
