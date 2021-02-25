from random import randint as get_rand

def create_matrix(length):
    rows = []
    for _ in range(length):
        tmp = []
        for _ in range(length):
            tmp.append(get_rand(0, 10))
        rows.append(tmp)

    return rows

print(create_matrix(5))

matrix = create_matrix(4, 4)

def calc_my_sum(matrix):
    count = 0
    sum = 0
    for parentlist in matrix:
        for matrixitem in parentlist:
            count += 1
            sum += matrixitem
    return sum / count

print(matrix)
average = calc_my_sum(matrix)
print(average)

def calc_element(matrix, average):
    count = 0
    for parentindex, parentlist in enumerate(matrix):
        print(f"parentInx: {parentindex}, parent: {parentlist}")
        for childindex, child in enumerate(parentlist):
            if child < average:
                continue
            if (parentind + childind) % 2 != 0:
                continue
            print(f'found! p-in{parentind}, ch-in{childind}, value{child}')
            count += 1
    return count

print(calc_element(matrix, average))
