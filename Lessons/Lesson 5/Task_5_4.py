from random import randint as get_rand

def create_matrix(length):
    rows = []
    for _ in range(length):
        tmp = []
        for _ in range(length):
            tmp.append(get_rand(0, 10))
            rows.append(tmp)

    return rows


def count_in_matrix(matrix, to_find):
    count = 0
    for parentlist in matrix:
        for matrixitem in parentlist:
            if matrixitem = to_find:
                count += 1
    return count

matrix = create_matrix(2, 3)
print(matrix)
print(count_in_matrix(matrix, 3))