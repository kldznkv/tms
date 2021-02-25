from random import randint as get_rand

def create_matrix(length):
    rows = []
    for _ in range(length):
        tmp = []
        for _ in range(length):
            tmp.append(get_rand(0, 10))
        rows.append(tmp)

    return rows

def count_of_matrix_elements(matrix):
    count = 0
    sum = 0
    for parentlist in matrix
        for matrixitem in parentlist
            count += 1
            sum += matrixitem
    return sum / count

print(matrix)


