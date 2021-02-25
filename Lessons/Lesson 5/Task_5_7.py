lst = ['Петрова', 'Сидорова']
def print_lastnames(names):
    for name in names:
        if name[0] == 'П' and name[-1] == 'а':
            print(name)
    return names
print(print_lastnames)