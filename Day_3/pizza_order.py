print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

bill = 0

if size == "S":
    print("Small Pizza: $15")
    bill += 15
elif size == "L":
    print("Medium Pizza: $20")
    bill += 20
elif size == "M":
    print("Large Pizza: $25")
else:
    print("Error")

if add_pepperoni == "Y" and size == "S":
    print("Pepperoni for Small Pizza: +$2")
    bill += 2
elif add_pepperoni == "Y" and (size == "M" or size == "L"):
    print("Pepperoni for Small Pizza: +$3")
    bill += 3

if extra_cheese == "Y":
    print("Extra cheese for any size pizza: + $1")
    bill += 1

print(f"Total bill ${bill}")
