acc = 0
while True:
    num = input("enter num: ")
    if not num.isdigit():
        if num == 'stop':
            break
            continue

            num = int(num)
            if num % 5 == 0:
                continue
            acc += int(num)

print(acc)
