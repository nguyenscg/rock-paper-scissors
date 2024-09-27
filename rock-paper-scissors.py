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

# 0 = rock, 1 = paper, # 2 = scissors

# how to decide if someone were to win or lose?

# how to choose random shape
print("Let's play Rock, Paper, Scissors!")
user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors"))

# random number from 0 to 2, include 2
computer_choice = random.randint(0, 2)
print(f"Computer picked {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice == computer_choice:
    print("It's a draw!")
else:
    print("Invalid choice, you lost. Try again!")


