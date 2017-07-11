import statistics

admins = {'Python':'Pass123@', 'user2':'paSS2'}

studentDict ={'Jeff':[78,88,93],
              'Alex':[92,99,96],
              'Sam':[89,76,78] }

def enterGrades():
    nameToEnter = input('What is the student name?')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade....')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist.')

def removeStudent():
    nameToRemove = input('What student do you want to remove?')
    if nameToRemove in studentDict:
        print('Removing student...')
        del studentDict[nameToRemove]
    else:
        print('Student does not exist')


def studentAVGs():
    for student in studentDict:
        gradeList = studentDict[student]
        averageGrade = statistics.mean(gradeList)
        print(student, 'has an average grade of:', averageGrade)

def main():
    print("""
        Welcome to Grade Central

	[1] - Enter Grades
	[2] - Remove Student
	[3] - Student Average Grades
	[4] - Exit
    """)
    action = input('What would you like to do today? (Enter a number)')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVGs()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given, try again')




login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('Welcome,', login)
        
        while True:
            main()
    else:
        print('Invalid password will detonate in 5 seconds.')

else:
    print('Invalid username, calling FBI to report')


