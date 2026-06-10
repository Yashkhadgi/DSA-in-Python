def setZeros(matrix):
    rows = set()
    cols = set()

    m = len(matrix)
    n = len(matrix[0])


    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0

    #user input
m = int(input("Enter no of rows:"))
n = int(input("Enter no of columns:"))

matrix = []

for i in range(m):
    row = list(map(int, input(f"Enter row {i+1}:").split()))
    matrix.append(row)

setZeros(matrix)

print("Output matrix:")
for row in matrix:
    print(row)