with open("file1.txt") as file:
    number_1 = file.readlines()
with open("file2.txt") as file:
    number_2 = file.readlines()

result = [int(num) for num in number_1 if num in number_2]


print(result)