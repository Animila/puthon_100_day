# water_level = 50
# if water_level > 50:
#     print('Drain water')
# else:
#     print("Continued")

print('Welcome to the molestation')
height = int(input("What is your height in cm?"))

if height >= 120:
    print("Welcome to the moles")

    age = int(input("What is your age? "))
    if age >= 18:
        bill = 18
        print("You buy 18$")
    elif 12 < age <18:
        bill = 14
        print("You buy 14")
    else:
        bill = 10
        print("You buy 10$")

    photo = input('Do you want a photo? (Y/N)')
    if photo.upper() == 'Y':
        bill += 3
    print(f"Your pay {bill}")
else:
    print("Pls exit on attraction")
