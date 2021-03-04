def unique(lst: list):
    seen = {}
    for i in lst:
        if not i in seen:
            seen[i] = 0
            continue
        seen[i] += 1
    return seen

if __name__== '__main__':
    print("Hello")
    print(unique([1, 22, 1, 3, 4, 5]))