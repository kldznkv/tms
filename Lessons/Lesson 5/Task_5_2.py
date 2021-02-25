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
