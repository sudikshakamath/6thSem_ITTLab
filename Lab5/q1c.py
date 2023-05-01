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

if cols1 != rows2:
    print("The matrices cannot be multiplied!")
else:
    result_matrix = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            row.append(0)
        result_matrix.append(row)

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    # Print the resulting matrix
    print("The result of multiplying the matrices is:")
    for row in result_matrix:
        print(row)