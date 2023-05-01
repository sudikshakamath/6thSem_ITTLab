n = int(input("Enter size of sets: "))

set1 = set()
set2 = set()

print("Enter elements of first set: ")
for i in range(n):
    set1.add(input())

print("Enter elements of second set: ")
for i in range(n):
    set2.add(input())

print("Union of sets is ", set1|set2)
print("Intersection of sets is ",set1&set2)
print("Difference of sets is ",set1-set2)
print("Symmetric Difference of sets is ",set1^set2)


