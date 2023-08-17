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
        print(matrix[i][j], end="\t")
    print() 
print("diagonal elements")
for i in range(rows):
    for j in range(cols):
        if (i==j):
            print(matrix[i][j],end="\t")
print("\n")
print("upper diagonal elements")
for i in range(rows):
    for j in range(cols):
        if (i<j):
            print(matrix[i][j],end="\t")
print("\n")
print("lower diagonal elements")
for i in range(rows):
    for j in range(cols):
        if (i>j):
            print(matrix[i][j],end="\t")
