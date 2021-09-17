student_score = input("Введите список оценок учеников: ").split()


for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

# Вводим максимальное значение
max_score = student_score[0]

# Начинаем логическую операцию на уровне сортировщика
for score in student_score:

    # если текущий элемент больше максимального значения
    # то приравниваем к максимальному значению текущий элемент

    if score > max_score:
        max_score = score


print(f"Самый высокий балл в классе - {max_score}")
