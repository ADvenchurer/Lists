matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)
print(len(matrix))
print(len(matrix[0]))
print(matrix[2][2])
for i in range (3):
    for j in range(3):
        print(matrix[i][j])

matrix2 = []

for i in range (3):
    temp = []
    for j in range (3):
         num = int(input("What is the number do you want to add?"))
         temp.append(num)
    matrix2.append(temp)
print(matrix2)


for i in range (3):
    print(matrix[i][i])


matrixA = [[1,2],
           [3,4]]

matrixB = [[5,6],
           [7,8]]
addM = [[0,0],
        [0,0]]

for i in range(2):
    for j in range (2):
        addM[i][j] = matrixA[i][j]+matrixB[i][j]

print(addM)

multiplyM = [[0,0],
             [0,0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            multiplyM[i][j] = multiplyM + (matrixA[i][k] * matrixB[k][j])