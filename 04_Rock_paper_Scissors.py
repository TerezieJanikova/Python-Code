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
---'   ____)____
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

game_images = [rock, paper, scissors]

your_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_number >=0 and your_number <=2:
    print(game_images[your_number])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])


if your_number >=3 or your_number < 0:
    print("You typed an invalid number. You lose!")
elif your_number == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and your_number == 2:
    print("You lose!")
elif your_number > computer_choice:
    print("You win!")
elif computer_choice > your_number:
    print("You lose!")
elif computer_choice == your_number:
    print("It's a draw!")
