import random

random.seed(128)

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

###

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_integer = random.randint(0, 1)

if random_integer == 0:
    print("Tail")
elif random_integer == 1:
    print("Heads")