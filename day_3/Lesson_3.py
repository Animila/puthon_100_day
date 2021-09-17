height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = float(weight) / (float(height) ** 2)


if bmi < 18.5:
    print('Вы скелет')
elif 18.5 < bmi < 25:
    print("Вы очень худой")
elif 25 < bmi < 30:
    print("Вы норм")
elif 30 < bmi < 35:
    print("Вы полный")
elif 30 < bmi:
    print("Жирдяй")
else:
    print("Вы труп")