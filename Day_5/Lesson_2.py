student_heights = input("Введите список роста учеников: ").split()
height = 0
student = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


for i in student_heights:
    height += i
    student += 1

print(round(height / student))
