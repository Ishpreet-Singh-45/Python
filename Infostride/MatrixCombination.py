import numpy as np

import random


rows = int(input('Rows: '))
cols = int(input('Cols: '))
l = []

# This part is to generate a matrix of 0s and 1s
for _ in range(rows*cols):
  l.append(random.choice([0, 1]))

l = np.array(l) # conversion to array
matrix = l.reshape(rows, cols) # conversion to matrix


count = 0

# testing
# rows = 4
# cols = 5
# matrix = np.array([1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1])
# matrix = matrix.reshape(rows, cols)

# print the matrix generated by the system for view
print()
print(matrix)
print()


def check_next(matrix, i, j):
    global rows, cols
    if(i >= rows and j >= cols):
        return False

    elif matrix[i][j] == 1:
        return True
    return False

for i in range(rows):
    for j in range(cols):
        # print(i,j)
        if matrix[i][j] == 1:
            while(j < cols - 1): # to traverse through cols
                if check_next(matrix, i, j):
                    j += 1
                    matrix[i][j] = 0
                    continue
                else:
                    break

            while i < rows - 1: # to traverse through rows
                if check_next(matrix, i, j):
                    i += 1
                    matrix[i][j] = 0
                    continue
                else:
                    break
            count += 1
        else:
            continue


                    

print(count)