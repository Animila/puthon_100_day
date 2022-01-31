age = int(input("What is your current age?"))

left_age = 90 - age
day = left_age * 365
weeks = left_age * 52
moths = left_age * 12

print(f'You have {day} days, {weeks} weeks and {moths} moths left.')