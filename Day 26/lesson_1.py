# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
#
# print(new_list)

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Angela"
new_list1 = [letter for letter in name]
print(new_list1)

list = [number * 2 for number in range(1, 5)]
print(list)

# с проверкой
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_name = [name for name in names if len(name) < 5]
print(short_name)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_name = [name.upper() for name in names if len(name) > 5]
print(short_name)