programming_dictionary = {
    "Bug": "Это ошибка в программе в результате работы",
    "Function": "Часть кода, которую можно вызвать в любом месте кода",
    "Loop": "Действие, повторяющее каждый раз",
    123: "hello"
}

print(programming_dictionary["Bug"])
print(programming_dictionary[123])

programming_dictionary["hello"] = "Killing games"
print(programming_dictionary["hello"])
print(programming_dictionary)
print("####")

programming_dictionary["Bug"] = "Лол"
print(programming_dictionary)

print("####")

for key in programming_dictionary:
    print(key)
    print("\/")
    print(programming_dictionary[key])



print("####")

programming_dictionary = {}
print(programming_dictionary)

empty_dictionary = {}


