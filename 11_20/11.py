import numpy as np

with open('in_11.txt') as f:
    lines = f.read() 
lines = lines.split('\n')

matrix = [[int(x) for x in row.split()] for row in lines]

# for row in matrix:
#     print(row)

size = 20
max = 0
for i in range(0, size-4):
    for j in range(0, size-4):
        prod = 1
        for k in range(0, 4):
            prod *= matrix[i][j+k]
        if prod > max:
            max = prod
            
        prod = 1
        for k in range(0, 4):
            prod *= matrix[i+k][j]
        if prod > max:
            max = prod

        prod = 1
        for k in range(0, 4):
            prod *= matrix[i+k][j+k]
        if prod > max:
            max = prod

        if (j >= 3):
            for l in range(j, size):
                prod = 1
                for k in range(0, 4):
                    prod *= matrix[i+k][(l-k)]
                if prod > max:
                    max = prod

print(max)