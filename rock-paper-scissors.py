# import random module
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

images = [rock, paper, scissors]

# 0 = rock, 1 = paper, # 2 = scissors

# how to decide if someone were to win or lose?

# how to choose random shape
print("Let's play Rock, Paper, Scissors!")
user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors"))
print(images[user_choice])

# random number from 0 to 2, include 2
computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice, you lost. Try again!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")



