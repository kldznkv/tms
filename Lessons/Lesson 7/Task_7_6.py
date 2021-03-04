def sum_items(*args):
    if len(args) <= 0:
        return 0, 0
    acc = 0
    max = args[0]
    for item in args:
        acc += item
        if item > max:
            max = item
    return acc, max

print(sum_items(1, 2, 3, 4))


