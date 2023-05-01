rows1 = int(input("Enter the number of rows in the first matrix: "))
cols1 = int(input("Enter the number of columns in the first matrix: "))

matrix1 = []
print("Enter the elements of the first matrix row by row:")
for i in range(rows1):
    row = []
    for j in range(cols1):
        row.append(int(input()))
    matrix1.append(row)

rows2 = int(input("Enter the number of rows in the second matrix: "))
cols2 = int(input("Enter the number of columns in the second matrix: "))

matrix2 = []
print("Enter the elements of the second matrix row by row:")
for i in range(rows2):
    row = []
    for j in range(cols2):
        row.append(int(input()))
    matrix2.append(row)

result = []
if(rows1 != rows2 or cols1 != cols2):
    print("Matrices cannot be added!")
else:
    for i in range(rows1):
        row = []
        for j in range(cols1):
            element = matrix1[i][j]+matrix2[i][j]
            row.append(element)
        result.append(row)

print("Resultant matrix is: \n")
for row in result:
    print(row)
