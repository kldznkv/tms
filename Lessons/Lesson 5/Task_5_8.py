pupils = [{'firstname': 'You_1', 'Group': 54, 'Physics': 8, 'Informatics': 9, 'history': 10},
{'firstname': 'You_2', 'Group': 52, 'Physics': 3, 'Informatics': 7, 'history': 6},
{'firstname': 'You_3', 'Group': 32, 'Physics': 4, 'Informatics': 8, 'history': 5}]
def calc_avg_score(users):
    for user in users:
        av = (user['Physics'] + user['Informatics'] + user['history']) / 3
        user['score'] = av

calc_avg_score(pupils)

def print_good_students(students, needscore):
    for student in students:
        if student['score'] >= float(needscore):
            print(f'Good student is: {student[name]}')
print(print_good_students)