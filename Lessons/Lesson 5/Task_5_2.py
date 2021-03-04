from random import randint


def create_matrix(n, m):
    rows = []
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(randint(0, 10))
        rows.append(tmp)
    return rows


def main():
    x = create_matrix()
    print(x)



if __name__ == '__main__':
    main()
