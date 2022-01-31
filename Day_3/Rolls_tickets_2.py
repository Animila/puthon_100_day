print("welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can rude the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
        bill = 5
    elif age <= 18:
        print("Please pay $7")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Please pay $12")
        bill = 12

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3

    print(f"You need ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride")