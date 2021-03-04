def avv(*args, mean_type=True):
    acc = 0
    count = 0

    for item in args:
        count += 1
        if mean_type:
            acc += item
            continue
        acc += item

    if mean_type:
        return acc / count

    return acc *= (1/count)

print(avv(1, 2, 3, mean_type=False))