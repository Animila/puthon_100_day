year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 != 0:
            print("Обычный")
        else:
            print("Високосный")
    else:
        print("Високосный")
else:
    print("Обычный")