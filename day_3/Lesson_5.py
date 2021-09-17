print("Приветствую вас в Пиццерии Хазбир")
size = input("Какой формы вам взять пиццу? (S, M или L)\n")
add_pepperoni = input("Хотите ли вы пеперони? (Y или N)\n")
extra_cheezes = input("Добавить ли больше сыра? (Y или N)\n")
bill = 0

print(" ")
print("-------")

if size.upper() == "S":
    print("Маленькая пицца - 15$")
    bill += 15
elif size.upper() == "M":
    print("Средняя пицца - 20$")
    bill += 20
elif size.upper() == "L":
    print("Большая пицца - 25$")
    bill += 25

if add_pepperoni == "Y":
    print(" ")
    if size.upper() == "S":
        print("Пепперони для маленькой пиццы - 2$")
        bill += 2
    else:
        print("Пеперои для большой/средней пиццы - 3$")
        bill += 3

if extra_cheezes == "Y":
    print(" ")
    print("Допольнительный сыр - 1$")
    bill += 1

print("-------")
print(f"Ваш счет - {bill}$")