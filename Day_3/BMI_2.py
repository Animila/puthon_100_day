height = float(input("Your height in m: "))
weight = float(input("Your weight in kg: "))

BMI = round(weight / (height ** 2), 2)

if BMI <= 18.5:
    print(f"Your BMI {BMI} have a Underweight")
elif 18.5 < BMI < 25:
    print(f"Your BMI {BMI} have a Normal weight")
elif 25 < BMI < 30:
    print(f"Your BMI {BMI} have a Overweight")
elif 30 < BMI < 35:
    print(f"Your BMI {BMI} have a Obese")
else:
    print(f"Your BMI {BMI} have a Clinically obese")
