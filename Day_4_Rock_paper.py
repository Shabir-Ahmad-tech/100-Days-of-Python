# Day 4: Rock Paper Scissors
#========================================
# Explanation of this project:
# This project is a simple rock paper scissors game 
# that takes the user's choices as input and outputs the result.
#========================================

import random as rd

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

user_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = rd.randint(0, 2)

# Check invalid input
if user_choice < 0 or user_choice > 2:
    print("Invalid input.")
else:
    print("---- User ----")
    print(choices[user_choice])

    print("---- Computer ----")
    print(choices[computer_choice])

    if user_choice == computer_choice:
        print("Draw")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")

#==========================
#----Code Challenge 01-----
#==========================
rand_num = rd.randint(0, 1)
if rand_num == 0:
    print("Head")
else:
    print("Tail")


#==========================
#----Code Challenge 02-----
#==========================
friends = ["Ahmad", "Ali", "Omar", "Ola", "Sara"]
random_person_to_pay = rd.choice(friends)
print(random_person_to_pay + " is going to pay for the meal today")

#==== Anoher method for Challenge 02====
friends = ["Ahmad", "Ali", "Omar", "Ola", "Sara"]
random_index = rd.randint(0, len(friends) - 1)  # or we can use rd.ranint(0, 4)
print(friends[random_index] + " is going to pay for the meal today")