guest = int(input("Enter guests: "))
if guest >= 50:
    print('resturant')
elif guest > 20 and guest < 50:
    print('cafe')
elif guest <= 20 and guest > 0:
    print('home')
elif guest <= 0:
    print('Error')
else:
    print('try another number')