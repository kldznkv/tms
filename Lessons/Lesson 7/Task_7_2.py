from random import randint

def create_matrix(weight, height):
    matrix = []
    for _ in range(0, weight):
        row = []
        for _ in range(0, height):
            row.append(randint(0, 20))
        matrix.append(row)
    return matrix

print(create_matrix(2, 2))

def print_matrix(matrix):
    for vert in matrix:
        for item in vert:
            print(f"Element is \"{item}")

matrix = create_matrix(2, 2)
print(print_matrix(matrix))

def sum_matrix(matrix):
    acc = 0
    for vert in matrix:
        for item in vert:
            acc += item
    return acc

print(sum_matrix(matrix))

def min(matrix):
    min = matrix[0][0]
    for vert in matrix:
        for item in vert:
            if item < min:
                min = item
    return min

print(matrix)
print(min(matrix))

def max(matrix):
    max = matrix[0][0]
    for vert in matrix:
        for item in vert:
            if item > max:
                max = item
    return max

