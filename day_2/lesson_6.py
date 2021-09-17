age = int(input("What is your correct age?\n"))

new_age = 90 - age
day = 365
week = 52
mouth = 12

age_day = new_age * day
age_week = new_age * week
age_mouth = new_age * mouth

print(f'You have {age_day} day, {age_week} week, {age_mouth} mouth')
