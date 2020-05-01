from collections import namedtuple

n = int(input())
Student = namedtuple('Student', 'ID MARKS NAME CLASS')

data_set = []
colums = [str(i) for i in input().split(" ") if len(i) > 0]
for i in range(n):
    row = [str(i) for i in input().split(" ") if len(i) > 0]
    data = Student(
        ID=row[colums.index('ID')], 
        MARKS=row[colums.index('MARKS')],
        NAME=row[colums.index('NAME')],
        CLASS=row[colums.index('CLASS')]
    )
    data_set.append(data)

avg = sum(float(i.MARKS) for i in data_set) / n

print("{:.2f}".format(avg))