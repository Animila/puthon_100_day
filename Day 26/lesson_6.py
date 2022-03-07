import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
student_score = {student:random.randint(1, 100) for student in names}
print(student_score)

passed_student = {students:score for students, score in student_score.items() if score >= 60}
print(passed_student)
