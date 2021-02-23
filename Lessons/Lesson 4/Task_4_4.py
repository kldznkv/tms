num = int(input('enter num: '))

lst = range(num)
acc = 0

i = 0
while i < len(lst):
    acc += lst[i] ** 3
    i += 1
print(acc)