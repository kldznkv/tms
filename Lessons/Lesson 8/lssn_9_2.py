from functools import reduce

print(list(map(lambda x: x ** 2, [1, 2, 3])))

print(list(map(lambda x: str(x), [1, 2, 3])))

result = filter(lambda x: x > 4, [1,2,3,4,5,6])
print(list(result))

result = filter(lambda x: 'k' in x, ["Lesha", "Leshka"])
print(list(result))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered = list(filter(lambda x: x %3 == 0, nums))
result = reduce(lambda x, y: x * y, filtered)

print(result)
print(reduce(lambda x, y: x * y, filter(lambda x: x %3 == 0, nums)))