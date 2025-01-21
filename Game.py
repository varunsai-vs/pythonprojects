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
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_input = int(input())
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)
else:
    print("Please enter the correct input")

print("Computer chose:")

import random
computer_input = random.randint(0,2)
if computer_input == 0:
    print(rock)
elif computer_input == 1:
    print(paper)
else:
    print(scissors)

if user_input == computer_input:
    print("It's a draw")
elif user_input == 0 and computer_input == 1:
    print("You Lose!")
elif user_input == 1 and computer_input == 2:
    print("you Lose!")
elif user_input == 2 and computer_input == 0:
    print("You Lose!")
else:
    print("You Win!")

