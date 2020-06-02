#Exercise to training lists
#Program that you can put the students and your grades

grade = []
repository = []
student = []

while True:
    student.append(input('Type the student name: '))
    grade.append(int(input('Type first grade: ')))
    grade.append(int(input('Type de second grade: ')))
    student.append(grade[:])
    grade.clear()
    repository.append(student[:])
    student.clear()
    print(repository)

    cont = input('Type "N" to stop typing new students: ').upper()
    if cont == 'N':
        break

print('--'*30)
print(f'{"Id":<3} {"Name":<20} Middle')
for pos, value in enumerate(repository):
    middle = (repository[pos][1][0] + repository[pos][1][1])/2
    print(f'{pos:<3} {repository[pos][0]:.<20} {middle}')

print('--'*30)
while True:
    d = int(input('Which student do you want to see the grade detail?'))
    print(f'Grades of {repository[d][0]}: {repository[d][1]}')
    cont = input('Type "N" to stop seeing grades: ').upper()
    if cont == 'N':
        break
