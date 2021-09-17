# вводим значения (тип str)
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# переводим значения в цифровой тип данных и производим вычисления
bmi = float(weight) / (float(height) ** 2)

# переводим переменную в целочисленную
bmi_int = int(bmi)

print(bmi_int)

