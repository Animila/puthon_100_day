import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choose = [rock, Paper, Scissors]

choose_player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(choose[choose_player])

choose_comp = random.randint(0, 2)
print(choose_comp)
print("Computer chose:")
print(choose[choose_comp])

#(игрок - камень, комп - ножницы), (игрок - бумага, компьютер - камень), (игрок - ножницы, компьютер - бумага)
win = (choose_player == 0 and choose_comp == 2) or (choose_player == 1 and choose_comp == 0) or (choose_player == 2 and choose_comp == 1)

if choose_player == choose_comp:
    print("Ничья")
elif win:
    print("Игрок победил")
else:
    print("Игрок проиграл")
