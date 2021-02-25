domain = input("Введите email: ").split("@")
if len(domain) == 1:
    if domain[1] == "gmail.com":
        print(domain[0])
else:
    print(f"{domain[1]} is not supported")