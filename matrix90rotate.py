rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
print("enter the elements")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(print("enter [",i,"][",j,"]values :"))))
    matrix.append(row)
print("Matrix:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" \t")
    print()
print("Tranpose of that Matrix :")    

.transpose = []
for i in range(cols):
    temp_transpose = []
    for row in matrix:
        temp_transpose.append(row[i])
    transpose.append(temp_transpose)
for i in range(rows):
    for j in range(cols):
        print(transpose[i][j], end=" \t")
    print()
