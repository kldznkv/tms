# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 33, 14, 15, 16, 17, 18, 19]
max = 0
for i in lst:
    if i > max:
        max = i

new_lst = []

for i in lst:
    if i % 2 != 0:
        new_lst.append(i)
    elif i % 2 == 0:
        i = max
        new_lst.append(i)
print(new_lst)
