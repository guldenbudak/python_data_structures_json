import json

with open('/Users/gulden/Downloads/python_odevleri (1)/inputs/odev3_students.json') as file:
    data = json.load(file)
grade_count = {}
failed_students = []
class_average ={}
users = {}
result = []
for student in data:
    name = student['name']
    scores = student['scores']
    avg = sum(scores) / len(scores)
    avg_int = int(avg)
    if avg_int >= 85:
        grade = 'AA'

    elif 70 <= avg_int <= 84.9:
        grade = 'BB'

    elif 50 <= avg_int <= 69.9:
        grade = 'CC'

    elif avg_int <= 50:
        grade = 'FF'

    if grade == 'FF':
        failed_students.append(f"name: {name}, avg: {avg_int}, grade: {grade}")

    users = {
        "name": name,
        "avg": avg_int,
        "grade": grade
    }

    result.append(users)
    grade_count[grade] = grade_count.get(grade, 0) + 1

print(*result,sep='\n')
print(f"failed students: {failed_students}")
print(f"grade count: {grade_count}")

global_sum = 0
highest = 0
lowest = 50000

for student in result:
    global_sum += student['avg']

print(f"global sum: {global_sum} global average: {global_sum/len(result)}")

top_student = {}
bottom_student = {}
for student in result:
    avg = student['avg']
    name = student['name']

    user ={
        "name": name,
        "avg": avg,
    }

    if highest < student['avg']:
        highest = student['avg']
        top_student = user

    if lowest > student['avg']:
        lowest = student['avg']
        bottom_student = user


print(f"top student: {top_student}")
print(f"bottom student: {bottom_student}")