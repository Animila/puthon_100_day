import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# # перебор словаря
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

print()
# # перебор фрейм данных
# for (key, value) in student_data_frame.items():
#     print(value)

# перебор каждой строки фрейма данных
for (index, row) in student_data_frame.iterrows():
    # вывод всей строки
    print(row)
    print()
    # вывод всей строки со значением колонки студенты
    print(row.student)
    print()
    # вывод только нужного значения
    if row.student == "Angela":
        print('ОЦЕНКА АНДЖЕЛЫ: ',row.score)
        print()
