cars = [
    {
        'num': 'ee2',
        'since': 1992,
    },
    {
        'num': 'efs3',
        'since': 1994,
    },
    {
        'num': 'ee4',
        'since': 2002,
    }
]
print([car for car in cars if car['since'] > 2000])

