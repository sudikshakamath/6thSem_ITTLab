rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

print("Original Matrix:\n")
for row in matrix:
    print(row)

transpose = []

for j in range(columns):
    row = []
    for i in range(rows):
        element = matrix[i][j]
        row.append(element)
    transpose.append(row)

print("Transpose is: \n")
for row in transpose:
    print(row)
