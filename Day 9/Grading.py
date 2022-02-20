student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for names in student_scores:
    score = student_scores[names]
    if 90 < score:
        student_grades[names] = "Отлично"
    elif 81 <= score <= 90:
        student_grades[names] = "Хорошо"
    elif 71 <= score <= 80:
        student_grades[names] = "нормально"
    elif score <= 70:
        student_grades[names] = "Не очень"

print(student_grades)
