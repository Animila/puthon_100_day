print("Welcome to the tip calculation")
bill_total = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
person = int(input("How many people to split the bill? "))

bill_percentage = bill_total / 100 * percentage
bill_total = bill_percentage + bill_total
bill_total_person = round(bill_total / person, 3)

print(f'Each person should pay: ${bill_total_person}')