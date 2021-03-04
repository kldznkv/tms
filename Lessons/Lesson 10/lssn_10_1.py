def main():
    file = open('file')
    lines = []
    while True:
        line = file.readline()
        if not line:
            print(line)
            break
        lines.append(line)

    file.close()
    print(lines[0])
    print(lines[-1])
    print(lines[:2])
    print(lines[:])

with open('file') as my_file:
    for lines in my_file.readline()
        print(line)

if __name__ == '__main__':
    main()