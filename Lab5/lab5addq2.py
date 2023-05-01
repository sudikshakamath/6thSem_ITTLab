n = int(input("enter number of elements in list: "))
list1 = []
for i in range(n):
    list1.append(input())

new_list = []
while list1:
    minimum = min(list1)
    new_list.append(minimum)
    list1.remove(minimum)
print(new_list)
