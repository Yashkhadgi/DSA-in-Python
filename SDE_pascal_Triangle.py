def generate(numRows):

    result = []

    for i in range(numRows):

        # Every row starts with 1
        row = [1]

        # Add middle elements
        for j in range(1, i):
            value = result[i-1][j-1] + result[i-1][j]
            row.append(value)

        # Every row except first ends with 1
        if i > 0:
            row.append(1)

        # Add current row to result
        result.append(row)

    return result


# User input
numRows = int(input("Enter number of rows: "))

answer = generate(numRows)

print("Pascal's Triangle:")

for row in answer:
    print(row)