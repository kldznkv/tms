lst = [1, 2, 11, 33, 15, 100]

accum = 0

for item in lst:
    if item == 33:
        break

    if item > 10:
        accum += item
        print(accum)