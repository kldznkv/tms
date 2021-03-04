def fact_loop(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum

print(fact_loop(10))

def fact_rec(n):
    if n <= 1:
        return 1
    return n * fact_rec(n-1)

print(fact_rec(10))

def my_format(string, char='!'):
    result_string = f'{char}{string}{char}'
    return result_string

print(my_format('Hello'))

from random import randint

def create_matrix(weight=3, height=2):
    matrix = []
    for _ in range(0, weight):
        row = []
        for _ in range(0, height):
            row.append(randint(0, 10))
        matrix.append(row)
    return matrix

matrix = create_matrix(5, 5)

def sum(*args):
    print(args)
    acc = 0
    for i in args:
        acc += 1
    return acc

print(sum(1,2,3,4))

