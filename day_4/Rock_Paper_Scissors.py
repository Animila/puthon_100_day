import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# создание списка изображений
game_image = [rock, scissors, paper]

print("Добро пожаловать в игру камень, ножницы, бумага")

# Генерация входных данных
person = int(input("Выберите камень, ножницы или бумагу (1/2/3): "))
random_1 = random.random()
random.seed(random_1)
computer = random.randint(1, 3)

# Выбор изображения для каждого игрока
person_image = game_image[person - 1]
computer_image = game_image[computer - 1]
print(f"Вы выбрали:\n{person_image}")
print(f"Компьютер выбрал:\n{computer_image}")

# Победа, если:
# Камень - ножницы
# Ножницы - бумага
# Бумага - камень
win1 = (person == 1 and computer == 2)
win2 = (person == 2 and computer == 3)
win3 = (person == 3 and computer == 1)

# Подведение итогов игры
if win1 or win2 or win3:
    print("Вы победили")
elif person == computer:
    print("Ничья")
else:
    print("Вы проиграли")
