from random import randint as get_rand

def create_matrix(length):
    rows = []
    for _ in range(length):
        tmp = []
        for _ in range(length):
            tmp.append(get_rand(0, 10))
            rows.append(tmp)

    return rows

print(create_matrix(3))

def sum_of_matrix_elements_by_divider(matrix, divider):
    sum = 0
    for parentlist in matrix:
        for matrixitem in parentlist:
            if matrixitem % divider == 0:
                sum += matrixitem
        return sum
matrix = create_matrix(2)
print(matrix)
print(sum_of_matrix_elements_by_divider(matrix, 3))