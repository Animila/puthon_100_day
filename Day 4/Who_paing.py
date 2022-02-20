import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, separated by a coma.\n")
names = namesAsCSV.split(', ')

lenght_list = len(names)
var = random.randint(0, lenght_list-1)
print(f'{names[var]} is goind to buy the meal today!')

## 2 Version ##

var = random.choice(names)
print(var)